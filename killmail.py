import logging
from queue import Queue
from threading import Thread
from victim_name_fetcher import VictimNameFetcher
from attacker_name_fetcher import AttackerNameFetcher
from victim_ship_name_fetcher import VictimShipNameFetcher
from attacker_ship_name_fetcher import AttackerShipNameFetcher
from solar_system_name_fetcher_local import SolarSystemNameFetcherLocal
from region_name_fetcher import RegionNameFetcher



class Killmail:
    """just a temporary data object to collect all relevant datapoints before pushing the whole thing to the
     InfluxPusher Class"""

    def __init__(self, unprocessed_killmail):
        """I just do all the processing in the constructor since setters/getters a la JAVA doesnt really make sense for
        me in python.
        Also since this Object just hold data and doesnt have any functionality I chose to do it this way"""
        self.logger = logging.getLogger(__name__ + ".Killmail")

        # G E N E R I C S
        self.id = unprocessed_killmail['package']['killID']
        self.time = unprocessed_killmail['package']['killmail']['killmail_time']
        self.total_value = unprocessed_killmail['package']['zkb']['totalValue'] + 0.0

        # A T T A C K E R
        self.attacker_is_npc = unprocessed_killmail['package']['zkb']['npc']
        self.attacker_is_solo = unprocessed_killmail['package']['zkb']['solo']
        self.attacker_is_awox = unprocessed_killmail['package']['zkb']['awox']
        self.attacker_amount = len(unprocessed_killmail['package']['killmail']['attackers'])

        # V I C T I M
        self.victim_damage_taken = unprocessed_killmail['package']['killmail']['victim']['damage_taken']

        # T H R E A D S
        my_threads = []
        que = Queue()

        thread1 = Thread(name="attacker_ships", target=lambda q, arg1: q.put(AttackerShipNameFetcher(unprocessed_killmail).getNames()), args=(que, "this"))
        thread2 = Thread(name="attacker_names", target=lambda q, arg1: q.put(AttackerNameFetcher(unprocessed_killmail).getNames()), args=(que, "is"))
        thread3 = Thread(name="victim_ship", target=lambda q, arg1: q.put(VictimShipNameFetcher(unprocessed_killmail).getNames()), args=(que, "a"))
        thread4 = Thread(name="victim_names", target=lambda q, arg1: q.put(VictimNameFetcher(unprocessed_killmail).getNames()), args=(que, "thread"))
        thread5 = Thread(name="solar_name", target=lambda q, arg1: q.put(SolarSystemNameFetcherLocal(unprocessed_killmail).getNames()), args=(que, "!"))
        thread6 = Thread(name="region_name", target=lambda q, arg1: q.put(RegionNameFetcher(unprocessed_killmail).getNames()), args=(que, "?"))

        my_threads.append(thread1)
        my_threads.append(thread2)
        my_threads.append(thread3)
        my_threads.append(thread4)
        my_threads.append(thread5)
        my_threads.append(thread6)

        for entry in my_threads:
            entry.start()
            self.logger.debug("{} started".format(entry))

        for entry in my_threads:
            entry.join()
            self.logger.debug("{} joined".format(entry))

        local_queue = []
        for x in range(0, 6):
            local_queue.append(que.get())

        self.logger.debug("local_queue: {}".format(local_queue))

        # N A M E S

        for entry in local_queue:
            if entry["category"] is "attacker_ship":
                self.attacker_ship_names = entry["name"]
            if entry["category"] is "attacker_name":
                self.attacker_names = entry["name"]
            if entry["category"] is "victim_ship":
                self.victim_ship_name = entry["name"]
            if entry["category"] is "victim_name":
                self.victim_names = entry["name"]
            if entry["category"] is "solar_name":
                self.solar_system = entry["name"]
            if entry["category"] is "region_name":
                self.region_names = entry["name"]

        self.solar_system_name = self.solar_system[0]
        self.solar_system_security = self.solar_system[1]

        self.region_name = self.region_names[0]["name"]
        self.constellation_name = self.region_names[1]["name"]

        self.victim_char_name = self.victim_names["character"]
        self.victim_corp_name = self.victim_names["corporation"]
        self.victim_alliance_name = self.victim_names["alliance"]

        self.attacker_char_name = self.attacker_names["character"]
        self.attacker_corp_name = self.attacker_names["corporation"]
        self.attacker_alliance_name = self.attacker_names["alliance"]

        # L O G G E R
        self.logger.info("KillID: {}".format(self.id))
        self.logger.info("Killmail time: {}".format(self.time))
        self.logger.info("Total Value: {}".format(self.total_value))
        self.logger.info("Attacker Char: {}, Corp: {}, Alli: {}".format(self.attacker_char_name, self.attacker_corp_name, self.attacker_alliance_name))
        self.logger.info("Attacker ships: {}".format(self.attacker_ship_names))
        self.logger.info("Victim Char: {}, Corp: {}, Alli: {}".format(self.victim_char_name, self.victim_corp_name, self.victim_alliance_name))
        self.logger.info("Victim Ship: {}".format(self.victim_ship_name))
        self.logger.info("Solar System Name: {}".format(self.solar_system_name))
        self.logger.info("Solar System Security: {}".format(self.solar_system_security))
        self.logger.info("Region Name: {}".format(self.region_name))
        self.logger.info("Constellation Name: {}".format(self.constellation_name))

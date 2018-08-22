from logging import getLogger
from queue import Queue
from threading import Thread





class Killmail2:
    """just a temporary data object to collect all relevant datapoints before pushing the whole thing to the
     InfluxPusher Class"""

    def __init__(self, unprocessed_killmail):
        """I just do all the processing in the constructor since setters/getters a la JAVA doesnt really make sense for
        me in python.
        Also since this Object just hold data and doesnt have any functionality I chose to do it this way"""
        self.logger = getLogger(__name__ + ".Killmail")

        self.unprocessed_killmail = unprocessed_killmail

        # T H R E A D S
        my_main_threads = []
        que = Queue()

        my_main_threads.append(Thread(name="Attacker", target=lambda q, arg1: q.put(), args=(que, "this")))
        my_main_threads.append(Thread(name="Victim", target=lambda q, arg1: q.put(), args=(que, "this")))
        my_main_threads.append(Thread(name="FinalBlow", target=lambda q, arg1: q.put(), args=(que, "this")))
        my_main_threads.append(Thread(name="Geographic", target=lambda q, arg1: q.put(), args=(que, "this")))

        for thread in my_main_threads:
            thread.start()
            self.logger.debug("{} started".format(thread))

        for thread in my_main_threads:
            thread.join()
            self.logger.debug("{} joined".format(thread))

        self.local_queue = []
        for x in range(0, 4):
            self.local_queue.append(que.get())
        self.logger.debug("local_queue: {}".format(self.local_queue))

        # G E N E R I C S
        self.id = unprocessed_killmail['package']['killID']
        self.time = unprocessed_killmail['package']['killmail']['killmail_time']

        # V A L U E
        self.value_total = unprocessed_killmail['package']['zkb']['totalValue'] + 0.0
        self.value_fitted = unprocessed_killmail['package']['zkb']['fittedValue'] + 0.0
        self.value_ship = self.value_total - self.value_fitted

        # F I N A L   B L O W
        self.final_blow_damage
        self.final_blow_ship_id
        self.final_blow_ship_name
        self.final_blow__damage_percent
        self.final_blow_ship_group_id
        self.final_blow_ship_group_name

        # G E O G R A P H I C
        self.solar_system_id = unprocessed_killmail['package']['killmail']['solar_system_id']
        self.solar_system_name
        self.solar_system_security
        self.solar_system_class
        self.region_id
        self.region_name
        self.constellation_id
        self.constellation_name

        # V I C T I M
        self.victim_damage_taken
        self.victim_name_ids
        self.victim_names
        self.victim_char_name
        self.victim_corp_name
        self.victim_alliance_name
        self.victim_ship_id
        self.victim_ship_name
        self.victim_ship_group_id
        self.victim_ship_group_name

        # A T T A C K E R
        self.attacker_is_solo = unprocessed_killmail['package']['zkb']['solo']
        self.attacker_is_npc = unprocessed_killmail['package']['zkb']['npc']
        self.attacker_is_awox = unprocessed_killmail['package']['zkb']['awox']
        self.attacker_amount = len(unprocessed_killmail['package']['killmail']['attackers'])
        self.attacker_name_ids
        self.attacker_names
        self.attacker_char_names
        self.attacker_corp_names
        self.attacker_alliance_names
        self.attacker_ship_ids
        self.attacker_ship_names
        self.attacker_ship_group_ids
        self.attacker_ship_group_names


        # L O G G E R
        self.logger.info("ID: {}".format(self.id))
        self.logger.info("Time: {}".format(self.time))

        self.logger.info("Value Total: {}".format(self.value_total))
        self.logger.info("Value Fitted: {}".format(self.value_fitted))
        self.logger.info("Value Ship: {}".format(self.value_ship))

        self.logger.info("Final Blow Damage: {}".format(self.final_blow_damage))
        self.logger.info("Final Blow Damage Percent: {}".format(self.final_blow_damage_percent))
        self.logger.info("Final Blow Ship ID: {}".format(self.final_blow_ship_id))
        self.logger.info("Final Blow Ship Name: {}".format(self.final_blow_ship_name))
        self.logger.info("Final Blow Ship Group ID: {}".format(self.final_blow_ship_group_id))
        self.logger.info("Final Blow Ship Group Name: {}".format(self.final_blow_ship_group_name))

        self.logger.info("Solar System ID: {}".format(self.solar_system_id))
        self.logger.info("Solar System Name: {}".format(self.solar_system_name))
        self.logger.info("Solar System Security: {}".format(self.solar_system_security))
        self.logger.info("Solar System Class: {}".format(self.solar_system_class))
        self.logger.info("Region ID: {}".format(self.region_id))
        self.logger.info("Region Name: {}".format(self.region_name))
        self.logger.info("Constellation ID: {}".format(self.constellation_id))
        self.logger.info("Constellation Name: {}".format(self.constellation_name))

        self.logger.info("Victim Damage Taken: {}".format(self.victim_damage_taken))
        self.logger.info("Victim Name IDs: {}".format(self.victim_name_ids))
        self.logger.info("Victim Names: {}".format(self.victim_names))
        self.logger.info("Victim Char Name: {}".format(self.victim_char_name))
        self.logger.info("Victim Corp Name: {}".format(self.victim_corp_name))
        self.logger.info("Victim Alliance Name: {}".format(self.victim_alliance_name))
        self.logger.info("Victim Ship ID: {}".format(self.victim_ship_id))
        self.logger.info("Victim Ship Name: {}".format(self.victim_ship_name))
        self.logger.info("Victim Ship Group ID: {}".format(self.victim_ship_group_id))
        self.logger.info("Victim Ship Group Name: {}".format(self.victim_ship_group_name))

        self.logger.info("Attacker Is Solo: {}".format(self.attacker_is_solo))
        self.logger.info("Attacker Is Npc: {}".format(self.attacker_is_npc))
        self.logger.info("Attacker Is Awox: {}".format(self.attacker_is_awox))
        self.logger.info("Attacker Amount: {}".format(self.attacker_amount))
        self.logger.info("Attacker Name IDs: {}".format(self.attacker_name_ids))
        self.logger.info("Attacker Names: {}".format(self.attacker_names))
        self.logger.info("Attacker Char Names: {}".format(self.attacker_char_names))
        self.logger.info("Attacker Corp Names: {}".format(self.attacker_corp_names))
        self.logger.info("Attacker Alliance Names: {}".format(self.attacker_alliance_names))
        self.logger.info("Attacker Ship IDs: {}".format(self.attacker_ship_ids))
        self.logger.info("Attacker Ship Names: {}".format(self.attacker_ship_names))
        self.logger.info("Attacker Ship Group IDs: {}".format(self.attacker_ship_group_ids))
        self.logger.info("Attacker Ship Group Names: {}".format(self.attacker_ship_group_names))

    '''

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

        if 0.5 <= self.solar_system_security:
            self.system_class = "highsec"
        elif self.solar_system_security is -1.0 or 0 > self.solar_system_security > -0.99:
            self.system_class = "nullsec"
        elif 0 < self.solar_system_security < 0.5:
            self.system_class = "lowsec"
        else:
            self.system_class = "wormhole"

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
        self.logger.info("Victim Damage Taken: {}".format(self.victim_damage_taken))
        self.logger.info("Solar System Name: {}".format(self.solar_system_name))
        self.logger.info("Solar System Security: {}".format(self.solar_system_security))
        self.logger.info("Solar System Class: {}".format(self.system_class))
        self.logger.info("Region Name: {}".format(self.region_name))
        self.logger.info("Constellation Name: {}".format(self.constellation_name))
        '''

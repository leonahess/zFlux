from logging import getLogger
from queue import Queue
from threading import Thread
from src.name_fetcher_final_blow import NameFetcherFinalBlow
from src.name_fetcher_geographic import NameFetcherGeographic
from src.name_fetcher_victim import NameFetcherVictim
from src.name_fetcher_attacker import NameFetcherAttacker


class Killmail:
    """just a temporary data object to collect all relevant datapoints before pushing the whole thing to the
     InfluxPusher Class"""

    def __init__(self, unprocessed_killmail):
        """I just do all the processing in the constructor since setters/getters a la JAVA doesnt really make sense for
        me in python.
        Also since this Object just hold data and doesnt have any functionality I chose to do it this way"""
        self.logger = getLogger(__name__)

        self.unprocessed_killmail = unprocessed_killmail
        self.logger.debug(unprocessed_killmail)

        # O B J E C T S
        name_fetcher_final_blow_object = NameFetcherFinalBlow(unprocessed_killmail)
        name_fetcher_geographic_object = NameFetcherGeographic(unprocessed_killmail)
        name_fetcher_victim_object = NameFetcherVictim(unprocessed_killmail)
        name_fetcher_attacker_object = NameFetcherAttacker(unprocessed_killmail)

        # T H R E A D S
        my_main_threads = []
        que = Queue()

        my_main_threads.append(Thread(name="Attacker", target=lambda q, arg1: q.put(name_fetcher_attacker_object.return_results()), args=(que, "this")))
        my_main_threads.append(Thread(name="Victim", target=lambda q, arg1: q.put(name_fetcher_victim_object.return_results()), args=(que, "this")))
        my_main_threads.append(Thread(name="FinalBlow", target=lambda q, arg1: q.put(name_fetcher_final_blow_object.return_results()), args=(que, "this")))
        my_main_threads.append(Thread(name="Geographic", target=lambda q, arg1: q.put(name_fetcher_geographic_object.return_results()), args=(que, "this")))

        for thread in my_main_threads:
            thread.start()
            self.logger.debug("{} started".format(thread))

        for thread in my_main_threads:
            thread.join()
            self.logger.debug("{} joined".format(thread))

        self.all_the_names = {}

        for x in range(0, 4):
            self.all_the_names = {**self.all_the_names, **que.get()}

        self.logger.debug("All the Names: {}".format(self.all_the_names))

        # G E N E R I C S
        self.id = unprocessed_killmail['package']['killID']
        self.time = unprocessed_killmail['package']['killmail']['killmail_time']

        # V A L U E
        self.value_total = unprocessed_killmail['package']['zkb']['totalValue'] + 0.0
        self.value_fitted = unprocessed_killmail['package']['zkb']['fittedValue'] + 0.0
        self.value_ship = self.value_total - self.value_fitted

        # F I N A L   B L O W
        self.final_blow_damage = self.all_the_names["final_blow_damage"]
        self.final_blow_ship_id = self.all_the_names["final_blow_ship_id"]
        self.final_blow_ship_name = self.all_the_names["final_blow_ship_name"]
        self.final_blow_ship_group_id = self.all_the_names["final_blow_ship_group_id"]
        self.final_blow_ship_group_name = self.all_the_names["final_blow_ship_group_name"]

        # G E O G R A P H I C
        self.solar_system_id = self.all_the_names["solar_system_id"]
        self.solar_system_name = self.all_the_names["solar_system_name"]
        self.solar_system_security = self.all_the_names["solar_system_security"]
        self.solar_system_class = self.all_the_names["solar_system_class"]
        self.region_id = self.all_the_names["region_id"]
        self.region_name = self.all_the_names["region_name"]
        self.constellation_id = self.all_the_names["constellation_id"]
        self.constellation_name = self.all_the_names["constellation_name"]

        # V I C T I M
        self.victim_damage_taken = self.all_the_names["victim_damage_taken"]
        self.victim_char_id = self.all_the_names["victim_char_id"]
        self.victim_corp_id = self.all_the_names["victim_corp_id"]
        self.victim_alliance_id = self.all_the_names["victim_alliance_id"]
        self.victim_char_name = self.all_the_names["victim_char_name"]
        self.victim_corp_name = self.all_the_names["victim_corp_name"]
        self.victim_alliance_name = self.all_the_names["victim_alliance_name"]
        self.victim_ship_id = self.all_the_names["victim_ship_id"]
        self.victim_ship_name = self.all_the_names["victim_ship_name"]
        self.victim_ship_group_id = self.all_the_names["victim_ship_group_id"]
        self.victim_ship_group_name = self.all_the_names["victim_ship_group_name"]

        if self.victim_damage_taken != 0:
            self.final_blow_damage_percent = float(round((self.final_blow_damage / self.victim_damage_taken) * 100, 0))
        else:
            self.final_blow_damage_percent = float(0)

        # A T T A C K E R
        self.attacker_is_solo = unprocessed_killmail['package']['zkb']['solo']
        self.attacker_is_npc = unprocessed_killmail['package']['zkb']['npc']
        self.attacker_is_awox = unprocessed_killmail['package']['zkb']['awox']
        self.attacker_amount = len(unprocessed_killmail['package']['killmail']['attackers'])

        self.attacker_char_ids = self.all_the_names["attacker_char_ids"]
        self.attacker_corp_ids = self.all_the_names["attacker_corp_ids"]
        self.attacker_alliance_ids = self.all_the_names["attacker_alliance_ids"]
        self.attacker_char_names = self.all_the_names["attacker_char_names"]
        self.attacker_corp_names = self.all_the_names["attacker_corp_names"]
        self.attacker_alliance_names = self.all_the_names["attacker_alliance_names"]
        self.attacker_ship_ids = self.all_the_names["attacker_ship_ids"]
        self.attacker_ship_names = self.all_the_names["attacker_ship_names"]
        self.attacker_ship_group_ids = self.all_the_names["attacker_ship_group_ids"]
        self.attacker_ship_group_names = self.all_the_names["attacker_ship_group_names"]

        # L O G G E R
        self.logger.debug("ID: {}".format(self.id))
        self.logger.debug("Time: {}".format(self.time))

        self.logger.debug("Value Total: {}".format(self.value_total))
        self.logger.debug("Value Fitted: {}".format(self.value_fitted))
        self.logger.debug("Value Ship: {}".format(self.value_ship))

        self.logger.debug("Final Blow Damage: {}".format(self.final_blow_damage))
        self.logger.debug("Final Blow Damage Percent: {}".format(self.final_blow_damage_percent))
        self.logger.debug("Final Blow Ship ID: {}".format(self.final_blow_ship_id))
        self.logger.debug("Final Blow Ship Name: {}".format(self.final_blow_ship_name))
        self.logger.debug("Final Blow Ship Group ID: {}".format(self.final_blow_ship_group_id))
        self.logger.debug("Final Blow Ship Group Name: {}".format(self.final_blow_ship_group_name))

        self.logger.debug("Solar System ID: {}".format(self.solar_system_id))
        self.logger.debug("Solar System Name: {}".format(self.solar_system_name))
        self.logger.debug("Solar System Security: {}".format(self.solar_system_security))
        self.logger.debug("Solar System Class: {}".format(self.solar_system_class))
        self.logger.debug("Region ID: {}".format(self.region_id))
        self.logger.debug("Region Name: {}".format(self.region_name))
        self.logger.debug("Constellation ID: {}".format(self.constellation_id))
        self.logger.debug("Constellation Name: {}".format(self.constellation_name))

        self.logger.debug("Victim Damage Taken: {}".format(self.victim_damage_taken))
        self.logger.debug("Victim Char Name: {}".format(self.victim_char_name))
        self.logger.debug("Victim Corp Name: {}".format(self.victim_corp_name))
        self.logger.debug("Victim Alliance Name: {}".format(self.victim_alliance_name))
        self.logger.debug("Victim Ship ID: {}".format(self.victim_ship_id))
        self.logger.debug("Victim Ship Name: {}".format(self.victim_ship_name))
        self.logger.debug("Victim Ship Group ID: {}".format(self.victim_ship_group_id))
        self.logger.debug("Victim Ship Group Name: {}".format(self.victim_ship_group_name))

        self.logger.debug("Attacker Is Solo: {}".format(self.attacker_is_solo))
        self.logger.debug("Attacker Is Npc: {}".format(self.attacker_is_npc))
        self.logger.debug("Attacker Is Awox: {}".format(self.attacker_is_awox))
        self.logger.debug("Attacker Amount: {}".format(self.attacker_amount))
        self.logger.debug("Attacker Char Names: {}".format(self.attacker_char_names))
        self.logger.debug("Attacker Corp Names: {}".format(self.attacker_corp_names))
        self.logger.debug("Attacker Alliance Names: {}".format(self.attacker_alliance_names))
        self.logger.debug("Attacker Ship IDs: {}".format(self.attacker_ship_ids))
        self.logger.debug("Attacker Ship Names: {}".format(self.attacker_ship_names))
        self.logger.debug("Attacker Ship Group IDs: {}".format(self.attacker_ship_group_ids))
        self.logger.debug("Attacker Ship Group Names: {}".format(self.attacker_ship_group_names))

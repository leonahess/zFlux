import logging
from victim_name_fetcher import VictimNameFetcher
from attacker_name_fetcher import AttackerNameFetcher
from solar_system_name_fetcher import SolarSystemNameFetcher
from victim_ship_name_fetcher import VictimShipNameFetcher
from attacker_ship_name_fetcher import AttackerShipNameFetcher


class Killmail:
    """just a temporary data object to collect all relevant datapoints before pushing the whole thing to the
     InfluxPusher Class"""

    def __init__(self, unprocessed_killmail):
        """I just do all the processing in the constructor since setters/getters a la JAVA doesnt really make sense for
        me in python.
        Also since this Object just hold data and doesnt have any functionality I chose to do it this way"""
        self.logger = logging.getLogger(__name__ + ".Killmail")

        self.id = unprocessed_killmail['package']['killID']
        self.time = unprocessed_killmail['package']['killmail']['killmail_time']
        self.solar_system_id = unprocessed_killmail['package']['killmail']['solar_system_id']
        self.total_value = unprocessed_killmail['package']['zkb']['totalValue'] + 0.0

        self.attacker_is_npc = unprocessed_killmail['package']['zkb']['npc']
        self.attacker_is_solo = unprocessed_killmail['package']['zkb']['solo']
        self.attacker_is_awox = unprocessed_killmail['package']['zkb']['awox']
        self.attacker_amount = len(unprocessed_killmail['package']['killmail']['attackers'])
        self.attacker_ship_names = AttackerShipNameFetcher(unprocessed_killmail).fetchNameWithId()

        self.victim_ship_id = unprocessed_killmail['package']['killmail']['victim']['ship_type_id']
        self.victim_ship_name = VictimShipNameFetcher(unprocessed_killmail).fetchNameWithId()
        self.victim_damage_taken = unprocessed_killmail['package']['killmail']['victim']['damage_taken']

        self.attacker_names = AttackerNameFetcher(unprocessed_killmail).fetchNameWithId()
        self.victim_names = VictimNameFetcher(unprocessed_killmail).fetchNameWithId()
        self.solar_system_name = SolarSystemNameFetcher(unprocessed_killmail).fetchNameWithId()

        self.logger.info("KillID: {}".format(self.id))
        self.logger.debug("Killmail time: {}".format(self.time))
        self.logger.debug("SolarID: {}".format(self.solar_system_id))
        self.logger.debug("Total Value".format(self.total_value))
        self.logger.debug("victim ship id: {}".format(self.victim_ship_id))
        self.logger.debug("Attacker Names: {}".format(self.attacker_names))
        self.logger.debug("Victim Names: {}".format(self.victim_names))
        self.logger.debug("Solar Name: {}".format(self.solar_system_name))

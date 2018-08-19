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

        # N A M E S
        self.attacker_ship_names = AttackerShipNameFetcher(unprocessed_killmail).fetchNameWithId()
        self.attacker_names = AttackerNameFetcher(unprocessed_killmail).getNames()
        self.victim_ship_name = VictimShipNameFetcher(unprocessed_killmail).fetchNameWithId()
        self.victim_names = VictimNameFetcher(unprocessed_killmail).getNames()

        self.solar_system_name = SolarSystemNameFetcher(unprocessed_killmail).getNames()

        self.victim_char_name = self.victim_names["character"]
        self.victim_corp_name = self.victim_names["corporation"]
        self.victim_alliance_name = self.victim_names["alliance"]

        self.attacker_char_name = self.attacker_names["character"]
        self.attacker_corp_name = self.attacker_names["corporation"]
        self.attacker_alliace_name = self.attacker_names["alliance"]

        # L O G G E R
        self.logger.info("KillID: {}".format(self.id))
        self.logger.debug("Killmail time: {}".format(self.time))
        self.logger.debug("Total Value".format(self.total_value))
        self.logger.debug("Attacker Char: {}, Corp: {}, Alli: {}".format(self.attacker_char_name, self.attacker_corp_name, self.attacker_alliace_name))
        self.logger.debug("Victim Char: {}, Corp: {}, Alli: {}".format(self.victim_char_name, self.victim_corp_name, self.victim_alliance_name))
        self.logger.debug("Solar Name: {}".format(self.solar_system_name))

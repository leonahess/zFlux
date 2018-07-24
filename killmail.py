from victim_name_fetcher import VictimNameFetcher
from attacker_name_fetcher import AttackerNameFetcher
from solar_system_name_fetcher import SolarSystemNameFetcher


class Killmail:

    def __init__(self, unprocessed_killmail):

        self.id = unprocessed_killmail['package']['killID']
        self.time = unprocessed_killmail['package']['killmail']['killmail_time']
        self.solar_system_id = unprocessed_killmail['package']['killmail']['solar_system_id']
        self.total_value = unprocessed_killmail['package']['zkb']['totalValue'] + 0.0

        self.attacker_is_npc = unprocessed_killmail['package']['zkb']['npc']
        self.attacker_is_solo = unprocessed_killmail['package']['zkb']['solo']
        self.attacker_is_awox = unprocessed_killmail['package']['zkb']['awox']
        self.attacker_amount = len(unprocessed_killmail['package']['killmail']['attackers'])

        self.victim_ship_id = unprocessed_killmail['package']['killmail']['victim']['ship_type_id']
        self.victim_damage_taken = unprocessed_killmail['package']['killmail']['victim']['damage_taken']

        self.attacker_names = AttackerNameFetcher(unprocessed_killmail).fetchNameWithId()
        self.victim_names = VictimNameFetcher(unprocessed_killmail).fetchNameWithId()
        self.solar_system_name = SolarSystemNameFetcher(unprocessed_killmail).fetchNameWithId()

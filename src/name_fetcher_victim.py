from src.name_fetcher2 import NameFetcher2


class NameFetcherVictim(NameFetcher2):

    def __init__(self, unprocessed_killmail):
        super().__init__(unprocessed_killmail)

        first_layer = self.extract_from_killmail()

        self.victim_char_id = first_layer['victim_char_id']
        self.victim_corp_id = first_layer['victim_corp_id']
        self.victim_alliance_id = first_layer['victim_alliance_id']
        self.victim_ship_id = first_layer['victim_ship_id']
        self.victim_damage_taken = first_layer['victim_damage_taken']

        second_layer = self.csv_inv_types_scraper([self.victim_ship_id])

        self.victim_ship_name = second_layer['name_list'][0]
        self.victim_ship_group_id = int(second_layer['group_id_list'][0])

        third_layer = self.csv_inv_groups_scraper([self.victim_ship_group_id])

        self.victim_ship_group_name = third_layer['group_name_list'][0]

        fourth_layer = self.make_esi_call([self.victim_char_id, self.victim_corp_id, self.victim_alliance_id])

        self.victim_char_name = ""
        self.victim_corp_name = ""
        self.victim_alliance_name = ""

        for entry in fourth_layer:
            if entry["category"] == "character":
                self.victim_char_name = entry["name"]
            if entry["category"] == "corporation":
                self.victim_corp_name = entry["name"]
            if entry["category"] == "alliance":
                self.victim_alliance_name = entry["name"]

    def extract_from_killmail(self):
        victim_char_id = ""
        victim_corp_id = ""
        victim_alliance_id = ""
        victim_ship_id = ""
        victim_damage_taken = ""

        if "character_id" in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_char_id = self.unprocessed_killmail['package']['killmail']['victim']['character_id']
        if "corporation_id" in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_corp_id = self.unprocessed_killmail['package']['killmail']['victim']['corporation_id']
        if "alliance_id" in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_alliance_id = self.unprocessed_killmail['package']['killmail']['victim']['alliance_id']
        if "ship_type_id" in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ship_id = self.unprocessed_killmail['package']['killmail']['victim']['ship_type_id']
        if "damage_taken" in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_damage_taken = self.unprocessed_killmail['package']['killmail']['victim']['damage_taken']

        return {
                "victim_char_id": victim_char_id,
                "victim_corp_id": victim_corp_id,
                "victim_alliance_id": victim_alliance_id,
                "victim_ship_id": victim_ship_id,
                "victim_damage_taken": victim_damage_taken
               }

    def return_results(self):
        return {
                "victim_char_id": self.victim_char_id,
                "victim_char_name": self.victim_char_name,
                "victim_corp_id": self.victim_corp_id,
                "victim_corp_name": self.victim_corp_name,
                "victim_alliance_id": self.victim_alliance_id,
                "victim_alliance_name": self.victim_alliance_name,
                "victim_damage_taken": self.victim_damage_taken,
                "victim_ship_id": self.victim_ship_id,
                "victim_ship_name": self.victim_ship_name,
                "victim_ship_group_id": self.victim_ship_group_id,
                "victim_ship_group_name": self.victim_ship_group_name
               }

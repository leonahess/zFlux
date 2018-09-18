from src.name_fetcher import NameFetcher


class NameFetcherAttacker(NameFetcher):

    def __init__(self, unprocessed_killmail):
        super().__init__(unprocessed_killmail)

        first_layer = self.extract_from_killmail()

        self.attacker_is_awox = first_layer['attacker_is_awox']
        self.attacker_is_npc = first_layer['attacker_is_npc']
        self.attacker_is_solo = first_layer['attacker_is_solo']
        self.attacker_amount = first_layer['attacker_amount']
        self.attacker_char_ids = first_layer['attacker_char_ids']
        self.attacker_corp_ids = first_layer['attacker_corp_ids']
        self.attacker_alliance_ids = first_layer['attacker_alliance_ids']
        self.attacker_ship_ids = first_layer['attacker_ship_ids']

        second_layer = self.csv_inv_types_scraper(self.attacker_ship_ids)

        self.attacker_ship_names = ""

        for x in range(0, len(second_layer['name_list'])):
            self.attacker_ship_names = self.attacker_ship_names + ";" + second_layer['name_list'][x]

        if self.attacker_ship_names is not "":
            self.attacker_ship_names = self.attacker_ship_names + ";"

        self.attacker_ship_group_ids = second_layer['group_id_list']

        third_layer = self.csv_inv_groups_scraper(self.attacker_ship_group_ids)

        self.attacker_ship_group_names = ""

        for x in range(0, len(third_layer['group_name_list'])):
            self.attacker_ship_group_names = self.attacker_ship_group_names + ";" + third_layer['group_name_list'][x]

        if self.attacker_ship_group_names is not "":
            self.attacker_ship_group_names = self.attacker_ship_group_names + ";"

        fourth_layer = self.make_esi_call(self.attacker_char_ids + self.attacker_corp_ids + self.attacker_alliance_ids)

        self.attacker_char_names = ""
        self.attacker_corp_names = ""
        self.attacker_alliance_names = ""

        for entry in fourth_layer:
            if entry["category"] == "character":
                self.attacker_char_names = self.attacker_char_names + ";" + entry["name"]
            if entry["category"] == "corporation":
                self.attacker_corp_names = self.attacker_corp_names + ";" + entry["name"]
            if entry["category"] == "alliance":
                self.attacker_alliance_names = self.attacker_alliance_names + ";" + entry["name"]

        if self.attacker_char_names is not "":
            self.attacker_char_names = self.attacker_char_names + ";"
        if self.attacker_corp_names is not "":
            self.attacker_corp_names = self.attacker_corp_names + ";"
        if self.attacker_alliance_names is not "":
            self.attacker_alliance_names = self.attacker_alliance_names + ";"

    def extract_from_killmail(self):

        attacker_is_awox = self.unprocessed_killmail['package']['zkb']['awox']
        attacker_is_npc = self.unprocessed_killmail['package']['zkb']['awox']
        attacker_is_solo = self.unprocessed_killmail['package']['zkb']['awox']
        attacker_amount = len(self.unprocessed_killmail['package']['killmail']['attackers'])
        attacker_char_ids = []
        attacker_corp_ids = []
        attacker_alliance_ids = []
        attacker_ship_ids = []

        for entry in self.unprocessed_killmail['package']['killmail']['attackers']:
            if "character_id" in entry and entry['character_id'] not in attacker_char_ids:
                attacker_char_ids.append(entry['character_id'])
            if "corporation_id" in entry and entry['corporation_id'] not in attacker_corp_ids:
                attacker_corp_ids.append(entry['corporation_id'])
            if "alliance_id" in entry and entry['alliance_id'] not in attacker_alliance_ids:
                attacker_alliance_ids.append(entry['alliance_id'])
            if "ship_type_id" in entry and entry['ship_type_id'] not in attacker_ship_ids:
                    attacker_ship_ids.append(entry['ship_type_id'])

        return {
                "attacker_is_awox": attacker_is_awox,
                "attacker_is_solo": attacker_is_solo,
                "attacker_is_npc": attacker_is_npc,
                "attacker_amount": attacker_amount,
                "attacker_char_ids": attacker_char_ids,
                "attacker_corp_ids": attacker_corp_ids,
                "attacker_alliance_ids": attacker_alliance_ids,
                "attacker_ship_ids": attacker_ship_ids
               }

    def return_results(self):
        self.logger.debug({
            "attacker_is_awox": self.attacker_is_awox,
            "attacker_is_solo": self.attacker_is_solo,
            "attacker_is_npc": self.attacker_is_npc,
            "attacker_amount": self.attacker_amount,
            "attacker_char_ids": self.attacker_char_ids,
            "attacker_corp_ids": self.attacker_corp_ids,
            "attacker_alliance_ids": self.attacker_alliance_ids,
            "attacker_ship_ids": self.attacker_ship_ids,
            "attacker_char_names": self.attacker_char_names,
            "attacker_corp_names": self.attacker_corp_names,
            "attacker_alliance_names": self.attacker_alliance_names,
            "attacker_ship_names": self.attacker_ship_names,
            "attacker_ship_group_ids": self.attacker_ship_group_ids,
            "attacker_ship_group_names": self.attacker_ship_group_names
        })

        return {
            "attacker_is_awox": self.attacker_is_awox,
            "attacker_is_solo": self.attacker_is_solo,
            "attacker_is_npc": self.attacker_is_npc,
            "attacker_amount": self.attacker_amount,
            "attacker_char_ids": self.attacker_char_ids,
            "attacker_corp_ids": self.attacker_corp_ids,
            "attacker_alliance_ids": self.attacker_alliance_ids,
            "attacker_ship_ids": self.attacker_ship_ids,
            "attacker_char_names": self.attacker_char_names,
            "attacker_corp_names": self.attacker_corp_names,
            "attacker_alliance_names": self.attacker_alliance_names,
            "attacker_ship_names": self.attacker_ship_names,
            "attacker_ship_group_ids": self.attacker_ship_group_ids,
            "attacker_ship_group_names": self.attacker_ship_group_names
        }

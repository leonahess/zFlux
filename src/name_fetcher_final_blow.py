from src.name_fetcher import NameFetcher


class NameFetcherFinalBlow(NameFetcher):

    def __init__(self, unprocessed_killmail):
        super().__init__(unprocessed_killmail)

        first_layer = self.extract_from_killmail()

        self.final_blow_damage = first_layer["damage_done"]
        self.final_blow_ship_id = first_layer["ship_type_id"]

        if self.final_blow_ship_id != "":
            second_layer = self.csv_inv_types_scraper([self.final_blow_ship_id])

            self.final_blow_ship_name = second_layer["name_list"][0]
            self.final_blow_ship_group_id = second_layer["group_id_list"][0]

            third_layer = self.csv_inv_groups_scraper([self.final_blow_ship_group_id])

            self.final_blow_ship_group_name = third_layer["group_name_list"][0]
        else:
            self.final_blow_ship_name = ""
            self.final_blow_ship_group_id = ""
            self.final_blow_ship_group_name = ""

    def extract_from_killmail(self):
        for entry in self.unprocessed_killmail['package']['killmail']['attackers']:
            if "final_blow" in entry and "damage_done" in entry and entry["final_blow"] is True and "ship_type_id" in entry:
                return {"damage_done": entry["damage_done"], "ship_type_id": entry["ship_type_id"]}
            if "final_blow" in entry and "damage_done" in entry and entry["final_blow"] is True:
                return {"damage_done": entry["damage_done"], "ship_type_id": ""}

        return {"damage_done": "", "ship_type_id": ""}

    def return_results(self):
        self.logger.debug({
                "final_blow_damage": self.final_blow_damage,
                "final_blow_ship_id": self.final_blow_ship_id,
                "final_blow_ship_name": self.final_blow_ship_name,
                "final_blow_ship_group_id": self.final_blow_ship_group_id,
                "final_blow_ship_group_name": self.final_blow_ship_group_name
               })

        return {
                "final_blow_damage": self.final_blow_damage,
                "final_blow_ship_id": self.final_blow_ship_id,
                "final_blow_ship_name": self.final_blow_ship_name,
                "final_blow_ship_group_id": self.final_blow_ship_group_id,
                "final_blow_ship_group_name": self.final_blow_ship_group_name
               }

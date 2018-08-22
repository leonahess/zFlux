from name_fetcher2 import NameFetcher2


class NameFetcherFinalBlow(NameFetcher2):

    def __init__(self):
        super().__init__(self)

        first_layer = self.get_first_layer()

        for entry in first_layer:
            if entry["category"] is "damage_done":
                self.damage_done = entry["value"]
            if entry["category"] is "ship_id":
                self.final_blow_ship_id = entry["value"]

    def get_first_layer(self):
        for entry in self.unprocessed_killmail['package']['killmail']['attackers']:
            if "final_blow" in entry and "damage_done" in entry and entry["final_blow"] is True:
                return [{"category": "damage_done", "value": entry["damage_done"]},
                        {"category": "ship_id", "value": entry["ship_type_id"]}]

        return [{"category": "damage_done", "value": None},
                {"category": "ship_id", "value": None}]

    def get_second_layer(self):


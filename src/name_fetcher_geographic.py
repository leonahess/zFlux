from src.name_fetcher import NameFetcher2


class NameFetcherGeographic(NameFetcher2):

    def __init__(self, unprocessed_killmail):
        super().__init__(unprocessed_killmail)

        first_layer = self.extract_from_killmail()

        self.solar_system_id = first_layer["solar_system_id"]

        second_layer = self.csv_map_solar_systems_scraper([self.solar_system_id])

        self.solar_system_name = second_layer["solar_system_name_list"][0]
        self.solar_system_security = round(float(second_layer["solar_system_security_list"][0]), 1)
        self.region_id = int(second_layer["region_id_list"][0])
        self.constellation_id = int(second_layer["constellation_id_list"][0])

        third_layer = self.make_esi_call([self.region_id, self.constellation_id])

        self.region_name = ""
        self.constellation_name = ""

        for entry in third_layer:
            if entry["category"] == "region":
                self.region_name = entry["name"]
            if entry["category"] == "constellation":
                self.constellation_name = entry["name"]

        if 0.5 <= self.solar_system_security:
            self.solar_system_class = "highsec"
        elif self.solar_system_security is -1.0 or 0 > self.solar_system_security > -0.99:
            self.solar_system_class = "nullsec"
        elif 0 < self.solar_system_security < 0.5:
            self.solar_system_class = "lowsec"
        else:
            self.solar_system_class = "wormhole"

    def extract_from_killmail(self):
        if "solar_system_id" in self.unprocessed_killmail['package']['killmail']:
            return {"solar_system_id": self.unprocessed_killmail['package']['killmail']["solar_system_id"]}
        return {"solar_system_id": ""}

    def return_results(self):
        return {
            "solar_system_id": self.solar_system_id,
            "solar_system_name": self.solar_system_name,
            "solar_system_security": self.solar_system_security,
            "solar_system_class": self.solar_system_class,
            "region_id": self.region_id,
            "region_name": self.region_name,
            "constellation_id": self.constellation_id,
            "constellation_name": self.constellation_name,

        }

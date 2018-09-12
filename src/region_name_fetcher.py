from src.name_fetcher import NameFetcher
import os
import csv


class RegionNameFetcher(NameFetcher):

    def generateIdList(self):
        region_id = ""
        constellation_id = ""

        filepath = os.path.dirname(__file__) + "/ressources/mapSolarSystems.csv"
        with open(filepath, newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                if row[2] == str(self.unprocessed_killmail["package"]["killmail"]["solar_system_id"]):
                    region_id = row[0]
                    constellation_id = row[1]

        return [region_id, constellation_id]

    def getNames(self):
        names_dict = self.fetchNameWithId()
        names = {"category": "region_name", "name": names_dict}
        return names

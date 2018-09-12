from old.name_fetcher import NameFetcher
import os
import csv


class SolarSystemNameFetcherLocal(NameFetcher):

    def generateIdList(self):
        solar_system_id = ""

        if "solar_system_id" in self.unprocessed_killmail["package"]["killmail"]:
            solar_system_id = self.unprocessed_killmail["package"]["killmail"]["solar_system_id"]

        return solar_system_id

    def fetchNameWithId(self):
        system_id = self.generateIdList()

        system_name = ""
        security_status = ""

        filepath = os.path.dirname(__file__) + "/ressources/mapSolarSystems.csv"
        with open(filepath, newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                if row[2] == str(system_id):
                    system_name = row[3]
                    security_status = float(row[21])

        self.logger.debug("Solar name list: {}".format(system_name))
        self.logger.debug("solar_name_str: {}".format(system_name))

        return [system_name, security_status]

    def getNames(self):
        names = self.fetchNameWithId()
        solar_system_name_dict = {"category": "solar_name", "name": names}
        return solar_system_name_dict

from name_fetcher import NameFetcher
import os
import csv


class SolarSystemNameFetcherLocal(NameFetcher):

    def __init__(self, unprocessed_killmail):
        NameFetcher.__init__(self, unprocessed_killmail)

    def generateIdList(self):
        solar_system_id = ""

        if "solar_system_id" in self.unprocessed_killmail["package"]["killmail"]:
            solar_system_id = self.unprocessed_killmail["package"]["killmail"]["solar_system_id"]

        return solar_system_id

    def extractNamesFromDict(self, names_dict):
        return names_dict

    def fetchNameWithId(self):
        system_id = self.generateIdList()

        system_name = ""

        filepath = os.path.dirname(__file__) + "/mapSolarSystems.csv"
        with open(filepath, newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                if row[2] == str(system_id):
                    system_name = row[3]

        self.logger.debug("Solar name list: {}".format(system_name))
        self.logger.debug("solar_name_str: {}".format(system_name))

        return system_name

    def getNames(self):
        names_dict = self.fetchNameWithId()
        names = self.extractNamesFromDict(names_dict)

        names_dict2 = {"category": "solar_name", "name": names}
        return names_dict2

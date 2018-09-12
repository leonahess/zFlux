import csv
import os
from old.name_fetcher import NameFetcher
from abc import abstractmethod


class ShipNameFetchter(NameFetcher):

    def __init__(self, unprocessed_killmail):
        NameFetcher.__init__(self, unprocessed_killmail)

    def fetchNameWithId(self):
        ship_name_str = ""
        ship_list = self.generateIdList()

        ship_name_list = []

        filepath = os.path.dirname(__file__) + "/ressources/invTypes.csv"
        with open(filepath, newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                for l in range(0, len(ship_list)):
                    if row[0] == str(ship_list[l]):
                        ship_name_list.append(row[2])
        self.logger.debug("Ship name list: {}".format(ship_name_list))

        for k in range(0, len(ship_name_list)):
            ship_name_str = ship_name_str + ';' + str(ship_name_list[k])
        ship_name_str = ship_name_str + ';'
        self.logger.debug("ship_name_str: {}".format(ship_name_str))

        return ship_name_str

    @abstractmethod
    def generateIdList(self):
        pass

from ship_name_fetcher import ShipNameFetchter


class VictimShipNameFetcher(ShipNameFetchter):

    def __init__(self, unprocessed_killmail):
        ShipNameFetchter.__init__(self, unprocessed_killmail)

    def generateIdList(self):
        victim_ship_list = list()
        
        if "ship_type_id" in self.unprocessed_killmail["package"]["killmail"]["victim"]:
            victim_ship_list.append(self.unprocessed_killmail["package"]["killmail"]["victim"]["ship_type_id"])

        return victim_ship_list

    def getNames(self):
        names_dict = self.fetchNameWithId()
        names = self.extractNamesFromDict(names_dict)

        names_dict2 = {"category": "victim_ship", "name": names}
        return names_dict2

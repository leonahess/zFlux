from src.ship_name_fetcher import ShipNameFetchter


class VictimShipNameFetcher(ShipNameFetchter):

    def generateIdList(self):
        victim_ship_list = list()
        
        if "ship_type_id" in self.unprocessed_killmail["package"]["killmail"]["victim"]:
            victim_ship_list.append(self.unprocessed_killmail["package"]["killmail"]["victim"]["ship_type_id"])

        return victim_ship_list

    def getNames(self):
        names = self.fetchNameWithId()
        victim_ship_names_dict = {"category": "victim_ship", "name": names}
        return victim_ship_names_dict

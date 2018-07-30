from name_fetcher import NameFetcher


class SolarSystemNameFetcher(NameFetcher):

    def __init__(self, unprocessed_killmail):
        NameFetcher.__init__(self, unprocessed_killmail)

    def generateIdList(self):
        solar_system_id = []

        if "solar_system_id" in self.unprocessed_killmail["package"]["killmail"]:
            solar_system_id.append(self.unprocessed_killmail["package"]["killmail"]["solar_system_id"])

        return solar_system_id

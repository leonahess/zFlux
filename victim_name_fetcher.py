from name_fetcher import NameFetcher


class VictimNameFetcher(NameFetcher):

    def generateIdList(self):
        victim_ids = []

        if 'character_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['character_id'])

        if 'corporation_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['corporation_id'])

        if 'alliance_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['alliance_id'])

        return victim_ids

    def getNames(self):
        names_dict = self.fetchNameWithId()
        names = self.extractNamesFromDict(names_dict)

        names_dict2 = {"category": "victim_name", "name": names}
        return names_dict2

    def extractNamesFromDict(self, names_dict):
        char_str = ""
        corp_str = ""
        alliance_str = ""

        for entry in names_dict:
            if "name" in entry and "character" in entry["category"]:
                char_str = entry["name"]
            if "name" in entry and "corporation" in entry["category"]:
                corp_str = entry["name"]
            if "name" in entry and "alliance" in entry["category"]:
                alliance_str = entry["name"]

        names = {"character": char_str, "corporation": corp_str, "alliance": alliance_str}

        return names

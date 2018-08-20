from name_fetcher import NameFetcher


class AttackerNameFetcher(NameFetcher):

    def __init__(self, unprocessed_killmail):
        NameFetcher.__init__(self, unprocessed_killmail)

    def generateIdList(self):
        attacker_ids = []

        for entry in self.unprocessed_killmail['package']['killmail']['attackers']:
            if 'character_id' in entry and entry['character_id'] not in attacker_ids:
                attacker_ids.append(entry['character_id'])
            if 'corporation_id' in entry and entry['corporation_id'] not in attacker_ids:
                attacker_ids.append(entry['corporation_id'])
            if 'alliance_id' in entry and entry['alliance_id'] not in attacker_ids:
                attacker_ids.append(entry['alliance_id'])

        return attacker_ids

    def getNames(self):
        names_dict = self.fetchNameWithId()
        names = self.extractNamesFromDict(names_dict)

        names_dict2 = {"category": "attacker_name", "name": names}
        return names_dict2

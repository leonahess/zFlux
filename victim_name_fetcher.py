from name_fetcher import NameFetcher


class VictimNameFetcher(NameFetcher):

    def __init__(self, unprocessed_killmail):
        NameFetcher.__init__(self, unprocessed_killmail)

    def generateIdList(self):
        victim_ids = []

        if 'character_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['character_id'])

        if 'corporation_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['corporation_id'])

        if 'alliance_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['alliance_id'])

        return victim_ids

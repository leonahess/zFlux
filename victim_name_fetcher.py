from name_fetcher import NameFetcher
from esi_call import EsiCall


class VictimNameFetcher(NameFetcher):

    def fetchNameWithId(self):

        victim_ids = []

        if 'character_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['character_id'])

        if 'corporation_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['corporation_id'])

        if 'alliance_id' in self.unprocessed_killmail['package']['killmail']['victim']:
            victim_ids.append(self.unprocessed_killmail['package']['killmail']['victim']['alliance_id'])

        names = EsiCall().makeCall(victim_ids)

        # logger.debug("Victim ids: {}".format(victim_ids))
        # logger.debug("Victim names: {}".format(names))

        return names

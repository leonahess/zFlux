from name_fetcher import NameFetcher
from esi_call import EsiCall


class AttackerNameFetcher(NameFetcher):

    def fetchNameWithId(self):
        attacker_ids = []

        for entry in self.unprocessed_killmail['package']['killmail']['attackers']:
            if 'character_id' in entry and entry['character_id'] not in attacker_ids:
                attacker_ids.append(entry['character_id'])
            if 'corporation_id' in entry and entry['corporation_id'] not in attacker_ids:
                attacker_ids.append(entry['corporation_id'])
            if 'alliance_id' in entry and entry['alliance_id'] not in attacker_ids:
                attacker_ids.append(entry['alliance_id'])

        if len(attacker_ids) < 1000 and len(attacker_ids) is not 0:
            names = EsiCall().makeCall(attacker_ids)
        else:
            names = []

        # logger.debug("Attacker attacker_ids: {}".format(attacker_ids))
        # logger.debug("Attacker names: {}".format(names))

        return names

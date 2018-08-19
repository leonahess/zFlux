from ship_name_fetcher import ShipNameFetchter


class AttackerShipNameFetcher(ShipNameFetchter):

    def __init__(self, unprocessed_killmail):
        ShipNameFetchter.__init__(self, unprocessed_killmail)

    def generateIdList(self):
        attacker_ship_list = list()

        for x in range(0, len(self.unprocessed_killmail['package']['killmail']['attackers'])):
            try:
                if self.unprocessed_killmail['package']['killmail']['attackers'][x]['ship_type_id'] not in attacker_ship_list:
                    attacker_ship_list.append(self.unprocessed_killmail['package']['killmail']['attackers'][x]["ship_type_id"])
            except KeyError as e:
                self.logger.error("attacker ship key error: {}".format(e))
        self.logger.debug("attacker_ship_list: {}".format(attacker_ship_list))

        return attacker_ship_list

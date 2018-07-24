import unittest

from killmail import Killmail
from attacker_name_fetcher import AttackerNameFetcher

class TestAttackerNameFetcher(unittest.TestCase):

    def setUp(self):
        uk1 = {"package":{"killID":71443648,"killmail":{"attackers":[{"alliance_id":1354830081,"character_id":992181402,"corporation_id":1324429368,"damage_done":4110,"final_blow":True,"security_status":-7.8,"ship_type_id":605,"weapon_type_id":2456}],"killmail_id":71443648,"killmail_time":"2018-07-24T17:56:14Z","solar_system_id":30003681,"victim":{"alliance_id":99007362,"character_id":2114300996,"corporation_id":98531953,"damage_taken":4110,"items":[{"flag":30,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":13,"item_type_id":8263,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":31,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":20,"item_type_id":380,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":32,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":11,"item_type_id":35770,"quantity_dropped":1,"singleton":0},{"flag":28,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":31,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":27,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":21,"item_type_id":380,"quantity_destroyed":1,"singleton":0},{"flag":32,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":28,"item_type_id":8089,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":5,"item_type_id":27381,"quantity_dropped":720,"singleton":0},{"flag":30,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":12,"item_type_id":22291,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":5971,"quantity_dropped":1,"singleton":0},{"flag":94,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":31608,"quantity_destroyed":1,"singleton":0}],"position":{"x":-456877791246.22,"y":-83876045685.746,"z":458094309170.23},"ship_type_id":32878}},"zkb":{"locationID":50006982,"hash":"9ab505bacad3122d8648e2c4aa9a3c80ad67eedc","fittedValue":2543013.41,"totalValue":7521431.46,"points":1,"npc":False,"solo":True,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"}}}

        self.k1 = Killmail(uk1)


    def testEmpty(self):
        self.assertEqual(AttackerNameFetcher(self.k1).fetchNameWithId(), [], "The returned List is not empty")

    def testMissingCharId(self):
        pass

    def testMissingCorpId(self):
        pass

    def testMissingAllianceId(self):
        pass

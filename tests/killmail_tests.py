import unittest
from killmail import Killmail


class TestKillmail(unittest.TestCase):

    def setUp(self):
        """
        uk1: full killmail

        uk2: no attacker alliance
        uk3: no attacker character
        uk4: no attacker corp

        uk5: no victim alliance
        uk6: no victim character
        uk7: no victim corp

        uk8: multiple attackers
        :return:
        """
        uk1 = {"package":{"killID":71443648,"killmail":{"attackers":[{"alliance_id":1354830081,"character_id":992181402,"corporation_id":1324429368,"damage_done":4110,"final_blow":True,"security_status":-7.8,"ship_type_id":605,"weapon_type_id":2456}],"killmail_id":71443648,"killmail_time":"2018-07-24T17:56:14Z","solar_system_id":30003681,"victim":{"alliance_id":99007362,"character_id":2114300996,"corporation_id":98531953,"damage_taken":4110,"items":[{"flag":30,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":13,"item_type_id":8263,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":31,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":20,"item_type_id":380,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":32,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":11,"item_type_id":35770,"quantity_dropped":1,"singleton":0},{"flag":28,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":31,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":27,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":21,"item_type_id":380,"quantity_destroyed":1,"singleton":0},{"flag":32,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":28,"item_type_id":8089,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":5,"item_type_id":27381,"quantity_dropped":720,"singleton":0},{"flag":30,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":12,"item_type_id":22291,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":5971,"quantity_dropped":1,"singleton":0},{"flag":94,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":31608,"quantity_destroyed":1,"singleton":0}],"position":{"x":-456877791246.22,"y":-83876045685.746,"z":458094309170.23},"ship_type_id":32878}},"zkb":{"locationID":50006982,"hash":"9ab505bacad3122d8648e2c4aa9a3c80ad67eedc","fittedValue":2543013.41,"totalValue":7521431.46,"points":1,"npc":False,"solo":True,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"}}}

        uk2 = {"package":{"killID":71443648,"killmail":{"attackers":[{"character_id":992181402,"corporation_id":1324429368,"damage_done":4110,"final_blow":True,"security_status":-7.8,"ship_type_id":605,"weapon_type_id":2456}],"killmail_id":71443648,"killmail_time":"2018-07-24T17:56:14Z","solar_system_id":30003681,"victim":{"alliance_id":99007362,"character_id":2114300996,"corporation_id":98531953,"damage_taken":4110,"items":[{"flag":30,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":13,"item_type_id":8263,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":31,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":20,"item_type_id":380,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":32,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":11,"item_type_id":35770,"quantity_dropped":1,"singleton":0},{"flag":28,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":31,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":27,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":21,"item_type_id":380,"quantity_destroyed":1,"singleton":0},{"flag":32,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":28,"item_type_id":8089,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":5,"item_type_id":27381,"quantity_dropped":720,"singleton":0},{"flag":30,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":12,"item_type_id":22291,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":5971,"quantity_dropped":1,"singleton":0},{"flag":94,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":31608,"quantity_destroyed":1,"singleton":0}],"position":{"x":-456877791246.22,"y":-83876045685.746,"z":458094309170.23},"ship_type_id":32878}},"zkb":{"locationID":50006982,"hash":"9ab505bacad3122d8648e2c4aa9a3c80ad67eedc","fittedValue":2543013.41,"totalValue":7521431.46,"points":1,"npc":False,"solo":True,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"}}}
        uk3 = {"package":{"killID":71443648,"killmail":{"attackers":[{"alliance_id":1354830081,"corporation_id":1324429368,"damage_done":4110,"final_blow":True,"security_status":-7.8,"ship_type_id":605,"weapon_type_id":2456}],"killmail_id":71443648,"killmail_time":"2018-07-24T17:56:14Z","solar_system_id":30003681,"victim":{"alliance_id":99007362,"character_id":2114300996,"corporation_id":98531953,"damage_taken":4110,"items":[{"flag":30,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":13,"item_type_id":8263,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":31,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":20,"item_type_id":380,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":32,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":11,"item_type_id":35770,"quantity_dropped":1,"singleton":0},{"flag":28,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":31,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":27,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":21,"item_type_id":380,"quantity_destroyed":1,"singleton":0},{"flag":32,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":28,"item_type_id":8089,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":5,"item_type_id":27381,"quantity_dropped":720,"singleton":0},{"flag":30,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":12,"item_type_id":22291,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":5971,"quantity_dropped":1,"singleton":0},{"flag":94,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":31608,"quantity_destroyed":1,"singleton":0}],"position":{"x":-456877791246.22,"y":-83876045685.746,"z":458094309170.23},"ship_type_id":32878}},"zkb":{"locationID":50006982,"hash":"9ab505bacad3122d8648e2c4aa9a3c80ad67eedc","fittedValue":2543013.41,"totalValue":7521431.46,"points":1,"npc":False,"solo":True,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"}}}
        uk4 = {"package":{"killID":71443648,"killmail":{"attackers":[{"alliance_id":1354830081,"character_id":992181402,"damage_done":4110,"final_blow":True,"security_status":-7.8,"ship_type_id":605,"weapon_type_id":2456}],"killmail_id":71443648,"killmail_time":"2018-07-24T17:56:14Z","solar_system_id":30003681,"victim":{"alliance_id":99007362,"character_id":2114300996,"corporation_id":98531953,"damage_taken":4110,"items":[{"flag":30,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":13,"item_type_id":8263,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":31,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":20,"item_type_id":380,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":32,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":11,"item_type_id":35770,"quantity_dropped":1,"singleton":0},{"flag":28,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":31,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":27,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":21,"item_type_id":380,"quantity_destroyed":1,"singleton":0},{"flag":32,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":28,"item_type_id":8089,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":5,"item_type_id":27381,"quantity_dropped":720,"singleton":0},{"flag":30,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":12,"item_type_id":22291,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":5971,"quantity_dropped":1,"singleton":0},{"flag":94,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":31608,"quantity_destroyed":1,"singleton":0}],"position":{"x":-456877791246.22,"y":-83876045685.746,"z":458094309170.23},"ship_type_id":32878}},"zkb":{"locationID":50006982,"hash":"9ab505bacad3122d8648e2c4aa9a3c80ad67eedc","fittedValue":2543013.41,"totalValue":7521431.46,"points":1,"npc":False,"solo":True,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"}}}

        uk5 = {"package":{"killID":71443648,"killmail":{"attackers":[{"alliance_id":1354830081,"character_id":992181402,"corporation_id":1324429368,"damage_done":4110,"final_blow":True,"security_status":-7.8,"ship_type_id":605,"weapon_type_id":2456}],"killmail_id":71443648,"killmail_time":"2018-07-24T17:56:14Z","solar_system_id":30003681,"victim":{"character_id":2114300996,"corporation_id":98531953,"damage_taken":4110,"items":[{"flag":30,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":13,"item_type_id":8263,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":31,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":20,"item_type_id":380,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":32,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":11,"item_type_id":35770,"quantity_dropped":1,"singleton":0},{"flag":28,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":31,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":27,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":21,"item_type_id":380,"quantity_destroyed":1,"singleton":0},{"flag":32,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":28,"item_type_id":8089,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":5,"item_type_id":27381,"quantity_dropped":720,"singleton":0},{"flag":30,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":12,"item_type_id":22291,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":5971,"quantity_dropped":1,"singleton":0},{"flag":94,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":31608,"quantity_destroyed":1,"singleton":0}],"position":{"x":-456877791246.22,"y":-83876045685.746,"z":458094309170.23},"ship_type_id":32878}},"zkb":{"locationID":50006982,"hash":"9ab505bacad3122d8648e2c4aa9a3c80ad67eedc","fittedValue":2543013.41,"totalValue":7521431.46,"points":1,"npc":False,"solo":True,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"}}}
        uk6 = {"package":{"killID":71443648,"killmail":{"attackers":[{"alliance_id":1354830081,"character_id":992181402,"corporation_id":1324429368,"damage_done":4110,"final_blow":True,"security_status":-7.8,"ship_type_id":605,"weapon_type_id":2456}],"killmail_id":71443648,"killmail_time":"2018-07-24T17:56:14Z","solar_system_id":30003681,"victim":{"alliance_id":99007362,"corporation_id":98531953,"damage_taken":4110,"items":[{"flag":30,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":13,"item_type_id":8263,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":31,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":20,"item_type_id":380,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":32,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":11,"item_type_id":35770,"quantity_dropped":1,"singleton":0},{"flag":28,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":31,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":27,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":21,"item_type_id":380,"quantity_destroyed":1,"singleton":0},{"flag":32,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":28,"item_type_id":8089,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":5,"item_type_id":27381,"quantity_dropped":720,"singleton":0},{"flag":30,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":12,"item_type_id":22291,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":5971,"quantity_dropped":1,"singleton":0},{"flag":94,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":31608,"quantity_destroyed":1,"singleton":0}],"position":{"x":-456877791246.22,"y":-83876045685.746,"z":458094309170.23},"ship_type_id":32878}},"zkb":{"locationID":50006982,"hash":"9ab505bacad3122d8648e2c4aa9a3c80ad67eedc","fittedValue":2543013.41,"totalValue":7521431.46,"points":1,"npc":False,"solo":True,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"}}}
        uk7 = {"package":{"killID":71443648,"killmail":{"attackers":[{"alliance_id":1354830081,"character_id":992181402,"corporation_id":1324429368,"damage_done":4110,"final_blow":True,"security_status":-7.8,"ship_type_id":605,"weapon_type_id":2456}],"killmail_id":71443648,"killmail_time":"2018-07-24T17:56:14Z","solar_system_id":30003681,"victim":{"alliance_id":99007362,"character_id":2114300996,"damage_taken":4110,"items":[{"flag":30,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":13,"item_type_id":8263,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":31,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":20,"item_type_id":380,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":29,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":32,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":11,"item_type_id":35770,"quantity_dropped":1,"singleton":0},{"flag":28,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":31,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":33,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":27,"item_type_id":8089,"quantity_dropped":1,"singleton":0},{"flag":21,"item_type_id":380,"quantity_destroyed":1,"singleton":0},{"flag":32,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":28,"item_type_id":8089,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":27381,"quantity_dropped":34,"singleton":0},{"flag":5,"item_type_id":27381,"quantity_dropped":720,"singleton":0},{"flag":30,"item_type_id":27381,"quantity_destroyed":34,"singleton":0},{"flag":12,"item_type_id":22291,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":5971,"quantity_dropped":1,"singleton":0},{"flag":94,"item_type_id":31153,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":31608,"quantity_destroyed":1,"singleton":0}],"position":{"x":-456877791246.22,"y":-83876045685.746,"z":458094309170.23},"ship_type_id":32878}},"zkb":{"locationID":50006982,"hash":"9ab505bacad3122d8648e2c4aa9a3c80ad67eedc","fittedValue":2543013.41,"totalValue":7521431.46,"points":1,"npc":False,"solo":True,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"}}}

        uk8 = {"package":{"killID":71445735,"killmail":{"attackers":[{"alliance_id":99007916,"character_id":1159571872,"corporation_id":98108528,"damage_done":194,"final_blow":False,"security_status":-2.2,"weapon_type_id":22456},{"alliance_id":99007916,"character_id":2113399727,"corporation_id":98557697,"damage_done":151,"final_blow":True,"security_status":-0.2,"ship_type_id":608,"weapon_type_id":564},{"alliance_id":99007916,"character_id":2113120595,"corporation_id":98557697,"damage_done":116,"final_blow":False,"security_status":5,"ship_type_id":11202,"weapon_type_id":11202},{"alliance_id":99007916,"character_id":93868335,"corporation_id":98442867,"damage_done":0,"final_blow":False,"security_status":4.7,"ship_type_id":621,"weapon_type_id":1877},{"alliance_id":99007916,"character_id":147559474,"corporation_id":98442867,"damage_done":0,"final_blow":False,"security_status":3,"ship_type_id":621,"weapon_type_id":1877},{"alliance_id":99007916,"character_id":95816687,"corporation_id":98565387,"damage_done":0,"final_blow":False,"security_status":0.4,"ship_type_id":32878,"weapon_type_id":8091},{"alliance_id":99007916,"character_id":1404839587,"corporation_id":98257549,"damage_done":0,"final_blow":False,"security_status":4.3,"ship_type_id":584,"weapon_type_id":9521},{"alliance_id":99007916,"character_id":1580968838,"corporation_id":98468592,"damage_done":0,"final_blow":False,"security_status":5,"ship_type_id":621,"weapon_type_id":1877},{"alliance_id":99007916,"character_id":2114045593,"corporation_id":98468592,"damage_done":0,"final_blow":False,"security_status":1.3,"ship_type_id":32878,"weapon_type_id":8091},{"alliance_id":99007916,"character_id":1818047222,"corporation_id":98257549,"damage_done":0,"final_blow":False,"security_status":5,"ship_type_id":621,"weapon_type_id":1875}],"killmail_id":71445735,"killmail_time":"2018-07-24T19:41:04Z","solar_system_id":30003688,"victim":{"alliance_id":99005680,"character_id":1573822593,"corporation_id":1003605409,"damage_taken":461,"items":[],"position":{"x":1294307890973.2,"y":179797633948.59,"z":-1229021760559},"ship_type_id":670}},"zkb":{"locationID":50008253,"hash":"419c87d58db8b08195c772b6681559d51af90feb","fittedValue":10000,"totalValue":10000,"points":1,"npc":False,"solo":False,"awox":False,"href":"https://esi.evetech.net/v1/killmails/71445735/419c87d58db8b08195c772b6681559d51af90feb/"}}}

        self.k1 = Killmail(uk1)
        self.k2 = Killmail(uk2)
        self.k3 = Killmail(uk3)
        self.k4 = Killmail(uk4)
        self.k5 = Killmail(uk5)
        self.k6 = Killmail(uk6)
        self.k7 = Killmail(uk7)
        self.k8 = Killmail(uk8)

    def testStatics(self):
        self.assertEqual(self.k1.id, 71443648, "The ID of the Killmail is wrong")
        self.assertEqual(self.k1.time, "2018-07-24T17:56:14Z", "The Time of the Killmail is wrong")
        self.assertEqual(self.k1.attacker_amount, 1, "Wrong amount of attackers")
        self.assertEqual(self.k8.attacker_amount, 10, "Wrong amount of attackers")
        self.assertEqual(self.k1.total_value, 7521431.46)
        self.assertEqual(self.k1.attacker_is_awox, False, "Bool is set wrong")
        self.assertEqual(self.k1.attacker_is_npc, False, "Bool is set wrong")
        self.assertEqual(self.k1.attacker_is_solo, True, "Bool is set wrong")
        self.assertEqual(self.k1.solar_system_id, 30003681, "SolarSystemID is wrong")

    def testnames(self):
        self.assertEqual(self.k1.attacker_names, [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                                                     {"category": "corporation", "id": 1324429368,
                                                      "name": "NED-Clan"},
                                                     {"category": "alliance", "id": 1354830081,
                                                      "name": "Goonswarm Federation"}], "Did not get the Expected attacker names")
        self.assertEqual(self.k1.victim_names,
                         [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}],
                         "Did not get the Expected victim names")

    def testMissingVictimCharId(self):
        self.assertEqual(self.k6.attacker_names, [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                                                     {"category": "corporation", "id": 1324429368,
                                                      "name": "NED-Clan"},
                                                     {"category": "alliance", "id": 1354830081,
                                                      "name": "Goonswarm Federation"}], "Did not get the Expected attacker names")
        self.assertEqual(self.k6.victim_names,
                         [{"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}],
                         "Did not get the Expected victim names")

    def testMissingVictimCorpId(self):
        self.assertEqual(self.k7.attacker_names, [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                                                     {"category": "corporation", "id": 1324429368,
                                                      "name": "NED-Clan"},
                                                     {"category": "alliance", "id": 1354830081,
                                                      "name": "Goonswarm Federation"}], "Did not get the Expected attacker names")
        self.assertEqual(self.k7.victim_names,
                         [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}],
                         "Did not get the Expected victim names")

    def testMissingVictimAllianceId(self):
        self.assertEqual(self.k5.attacker_names, [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                                                     {"category": "corporation", "id": 1324429368,
                                                      "name": "NED-Clan"},
                                                     {"category": "alliance", "id": 1354830081,
                                                      "name": "Goonswarm Federation"}], "Did not get the Expected attacker names")
        self.assertEqual(self.k5.victim_names,
                         [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"}],
                         "Did not get the Expected victim names")

    def testMissingAttackerCharId(self):
        self.assertEqual(self.k3.attacker_names, [{"category": "corporation", "id": 1324429368,
                                                    "name": "NED-Clan"},
                                                     {"category": "alliance", "id": 1354830081,
                                                      "name": "Goonswarm Federation"}], "Did not get the Expected attacker names")
        self.assertEqual(self.k3.victim_names,
                         [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}],
                         "Did not get the Expected victim names")

    def testMissingAttackerCorpId(self):
        self.assertEqual(self.k4.attacker_names, [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                                                     {"category": "alliance", "id": 1354830081,
                                                      "name": "Goonswarm Federation"}], "Did not get the Expected attacker names")
        self.assertEqual(self.k4.victim_names,
                         [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}],
                         "Did not get the Expected victim names")

    def testMissingAttackerAllianceId(self):
        self.assertEqual(self.k2.attacker_names, [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                                                     {"category": "corporation", "id": 1324429368,
                                                      "name": "NED-Clan"}],
                         "Did not get the Expected attacker names")
        self.assertEqual(self.k2.victim_names,
                         [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}],
                         "Did not get the Expected victim names")

from src.victim_name_fetcher import VictimNameFetcher
from tests.setup import Setup


class TestVictimNameFetcher(Setup):

    def setUp(self):
        super().setUp()
        self.k00 = VictimNameFetcher(self.uk10)

        self.k20 = VictimNameFetcher(self.uk20)
        self.k21 = VictimNameFetcher(self.uk21)
        self.k22 = VictimNameFetcher(self.uk22)
        self.k23 = VictimNameFetcher(self.uk23)
        self.k24 = VictimNameFetcher(self.uk24)
        self.k25 = VictimNameFetcher(self.uk25)
        self.k26 = VictimNameFetcher(self.uk26)
        self.k27 = VictimNameFetcher(self.uk27)
        self.k28 = VictimNameFetcher(self.uk28)

    def testEmpty(self):
        self.assertEqual(self.k28.getNames(), {"character": "", "corporation": "", "alliance": ""}, "Wrong Dict")
        self.assertEqual(self.k28.extractNamesFromDict(self.k28.fetchNameWithId()), {"character": "", "corporation": "", "alliance": ""}, "Wrong Dict")
        self.assertEqual(self.k28.fetchNameWithId(), [], "List should be empty")
        self.assertEqual(self.k28.generateIdList(), [], "List should be empty")

    def testMissingCharId(self):
        self.assertEqual(self.k20.getNames(),
                         {"character": "", "corporation": ";Rainbow Pegasus Squadron;",
                          "alliance": ";Ranger Regiment;"}, "Wrong Dict")
        self.assertEqual(self.k20.extractNamesFromDict(self.k20.fetchNameWithId()),
                         {"character": "", "corporation": ";Rainbow Pegasus Squadron;",
                          "alliance": ";Ranger Regiment;"}, "Wrong Dict")
        self.assertEqual(self.k20.fetchNameWithId(),
                         [{"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}], "List should be empty")
        self.assertEqual(self.k20.generateIdList(), [98531953, 99007362], "List should be empty")

    def testMissingCorpId(self):
        self.assertEqual(self.k22.getNames(),
                         {"character": ";Assassin Jx;", "corporation": "",
                          "alliance": ";Ranger Regiment;"}, "Wrong Dict")
        self.assertEqual(self.k22.extractNamesFromDict(self.k22.fetchNameWithId()),
                         {"character": ";Assassin Jx;", "corporation": "",
                          "alliance": ";Ranger Regiment;"}, "Wrong Dict")
        self.assertEqual(self.k22.fetchNameWithId(),
                         [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}], "List should be empty")
        self.assertEqual(self.k22.generateIdList(), [2114300996, 99007362], "List should be empty")

    def testMissingAllianceId(self):
        self.assertEqual(self.k24.getNames(),
                         {"character": ";Assassin Jx;", "corporation": ";Rainbow Pegasus Squadron;",
                          "alliance": ""}, "Wrong Dict")
        self.assertEqual(self.k24.extractNamesFromDict(self.k24.fetchNameWithId()),
                         {"character": ";Assassin Jx;", "corporation": ";Rainbow Pegasus Squadron;",
                          "alliance": ""}, "Wrong Dict")
        self.assertEqual(self.k24.fetchNameWithId(),
                         [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"}], "List should be empty")
        self.assertEqual(self.k24.generateIdList(), [2114300996, 98531953], "List should be empty")

    def testNoMissingStuff(self):
        self.assertEqual(self.k00.getNames(), {"character": ";Assassin Jx;", "corporation": ";Rainbow Pegasus Squadron;", "alliance": ";Ranger Regiment;"}, "Wrong Dict")
        self.assertEqual(self.k00.extractNamesFromDict(self.k00.fetchNameWithId()),
                         {"character": ";Assassin Jx;", "corporation": ";Rainbow Pegasus Squadron;", "alliance": ";Ranger Regiment;"}, "Wrong Dict")
        self.assertEqual(self.k00.fetchNameWithId(), [{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "corporation", "id": 98531953,
                           "name": "Rainbow Pegasus Squadron"},
                          {"category": "alliance", "id": 99007362,
                           "name": "Ranger Regiment"}], "List should be empty")
        self.assertEqual(self.k00.generateIdList(), [2114300996, 98531953, 99007362], "List should be empty")

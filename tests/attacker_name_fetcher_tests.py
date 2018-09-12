from tests.setup import Setup
from src.attacker_name_fetcher import AttackerNameFetcher


class TestAttackerNameFetcher(Setup):

    def setUp(self):
        super().setUp()

        self.k00 = AttackerNameFetcher(self.uk00)

        self.k10 = AttackerNameFetcher(self.uk10)
        self.k11 = AttackerNameFetcher(self.uk11)
        self.k12 = AttackerNameFetcher(self.uk12)
        self.k13 = AttackerNameFetcher(self.uk13)
        self.k14 = AttackerNameFetcher(self.uk14)
        self.k15 = AttackerNameFetcher(self.uk15)

        self.k30 = AttackerNameFetcher(self.uk30)
        self.k31 = AttackerNameFetcher(self.uk31)
        self.k32 = AttackerNameFetcher(self.uk32)
        self.k33 = AttackerNameFetcher(self.uk33)
        self.k34 = AttackerNameFetcher(self.uk34)
        self.k35 = AttackerNameFetcher(self.uk35)
        self.k36 = AttackerNameFetcher(self.uk36)
        self.k37 = AttackerNameFetcher(self.uk37)
        self.k38 = AttackerNameFetcher(self.uk38)
        self.k39 = AttackerNameFetcher(self.uk39)
        self.k40 = AttackerNameFetcher(self.uk40)
        self.k41 = AttackerNameFetcher(self.uk41)
        self.k42 = AttackerNameFetcher(self.uk42)

    def test_empty(self):
        self.k18 = AttackerNameFetcher(self.uk18)
        self.assertEqual(self.k18.getNames(), {"character": "", "corporation": "", "alliance": ""}, "Wrong Dict")
        self.assertEqual(self.k18.extractNamesFromDict(self.k18.fetchNameWithId()), {"character": "", "corporation": "", "alliance": ""}, "Wrong Dict")
        self.assertEqual(self.k18.fetchNameWithId(), [], "The returned List is not empty")
        self.assertEqual(self.k18.generateIdList(), [], "The returned List is not empty")

    def test_missingc_char_id(self):
        # 1 Attacker
        self.assertEqual(self.k10.getNames(), {"character": "", "corporation": ";NED-Clan;", "alliance": ";Goonswarm Federation;"}, "The returned Dict is wrong")
        self.assertEqual(self.k10.extractNamesFromDict(self.k10.fetchNameWithId()), {"character": "", "corporation": ";NED-Clan;", "alliance": ";Goonswarm Federation;"}, "The returned Dict is wrong")
        self.assertEqual(self.k10.fetchNameWithId(), [{"category": "corporation", "id": 1324429368,
                                                      "name": "NED-Clan"},
                                                    {"category": "alliance", "id": 1354830081,
                                                      "name": "Goonswarm Federation"}], "Wrong List")
        self.assertEqual(self.k10.generateIdList(), [1324429368, 1354830081], "Wrong List")

        # 2 Attacker 1 missing
        self.assertEqual(self.k31.getNames(),
                         {"character": ";Ailiece Ardua;",
                          "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                          "alliance": ";Jita Holding Inc.;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k31.extractNamesFromDict(self.k31.fetchNameWithId()),
                         {"character": ";Ailiece Ardua;",
                          "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                          "alliance": ";Jita Holding Inc.;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k31.fetchNameWithId(),
                         [{"category": "corporation", "id": 818601383,
                           "name": "The Reappropriation Committee"},
                          {"category": "alliance", "id": 99005382,
                           "name": "Jita Holding Inc."},
                          {'category': 'character', 'id': 91715917, 'name': 'Ailiece Ardua'},
                          {'category': 'corporation', 'id': 98567437, 'name': 'HC - georgieboys'}], "Wrong List")
        self.assertEqual(self.k31.generateIdList(), [818601383, 99005382, 91715917, 98567437], "Wrong List")

        # 2 attacker 2 missing
        self.assertEqual(self.k32.getNames(),
                         {"character": "",
                          "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                          "alliance": ";Jita Holding Inc.;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k32.extractNamesFromDict(self.k32.fetchNameWithId()),
                         {"character": "",
                          "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                          "alliance": ";Jita Holding Inc.;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k32.fetchNameWithId(),
                         [{"category": "corporation", "id": 818601383,
                           "name": "The Reappropriation Committee"},
                          {"category": "alliance", "id": 99005382,
                           "name": "Jita Holding Inc."},
                          {'category': 'corporation', 'id': 98567437, 'name': 'HC - georgieboys'}], "Wrong List")
        self.assertEqual(self.k32.generateIdList(), [818601383, 99005382, 98567437], "Wrong List")

    def test_missing_corp_id(self):
        self.assertEqual(self.k12.getNames(),
                         {"character": ";Strife Senior;", "corporation": "", "alliance": ";Goonswarm Federation;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k12.extractNamesFromDict(self.k12.fetchNameWithId()),
                         {"character": ";Strife Senior;", "corporation": "", "alliance": ";Goonswarm Federation;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k12.fetchNameWithId(), [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                                                     {"category": "alliance", "id": 1354830081,
                                                      "name": "Goonswarm Federation"}], "Wrong List")
        self.assertEqual(self.k12.generateIdList(), [992181402, 1354830081], "Wrong List")

    def test_missing_alliance_id(self):
        self.assertEqual(self.k14.getNames(),
                         {"character": ";Strife Senior;", "corporation": ";NED-Clan;", "alliance": ""},
                         "The returned Dict is wrong")
        self.assertEqual(self.k14.extractNamesFromDict(self.k14.fetchNameWithId()),
                         {"character": ";Strife Senior;", "corporation": ";NED-Clan;", "alliance": ""},
                         "The returned Dict is wrong")
        self.assertEqual(self.k14.fetchNameWithId(), [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                                                     {"category": "corporation", "id": 1324429368,
                                                      "name": "NED-Clan"}], "Wrong List")
        self.assertEqual(self.k14.generateIdList(), [992181402, 1324429368], "Wrong List")

    def test_no_missing_stuff(self):
        self.assertEqual(self.k00.getNames(),
                         {"character": ";Strife Senior;", "corporation": ";NED-Clan;", "alliance": ";Goonswarm Federation;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k00.extractNamesFromDict(self.k00.fetchNameWithId()),
                         {"character": ";Strife Senior;", "corporation": ";NED-Clan;", "alliance": ";Goonswarm Federation;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k00.fetchNameWithId(),
                         [{"category": "character", "id": 992181402, "name": "Strife Senior"},
                          {"category": "corporation", "id": 1324429368,
                           "name": "NED-Clan"},
                          {"category": "alliance", "id": 1354830081,
                           "name": "Goonswarm Federation"}], "Wrong List")
        self.assertEqual(self.k00.generateIdList(), [992181402, 1324429368, 1354830081], "Wrong List")

    def test_multiple_attackers_no_missing_stuff(self):
        self.assertEqual(self.k30.getNames(),
                         {"character": ";Shotgun Pimp;Ailiece Ardua;", "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                          "alliance": ";Jita Holding Inc.;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k30.extractNamesFromDict(self.k30.fetchNameWithId()),
                         {"character": ";Shotgun Pimp;Ailiece Ardua;", "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                          "alliance": ";Jita Holding Inc.;"},
                         "The returned Dict is wrong")
        self.assertEqual(self.k30.fetchNameWithId(),
                         [{"category": "character", "id": 224182597, "name": "Shotgun Pimp"},
                          {"category": "corporation", "id": 818601383,
                           "name": "The Reappropriation Committee"},
                          {"category": "alliance", "id": 99005382,
                           "name": "Jita Holding Inc."},{'category': 'character', 'id': 91715917, 'name': 'Ailiece Ardua'},
 {'category': 'corporation', 'id': 98567437, 'name': 'HC - georgieboys'}], "Wrong List")
        self.assertEqual(self.k30.generateIdList(), [224182597, 818601383, 99005382, 91715917, 98567437] , "Wrong List")

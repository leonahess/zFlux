from tests.setup import Setup
from old.killmail import Killmail
from old.attacker_name_fetcher import AttackerNameFetcher


class TestKillmailStatics(Setup):

    def setUp(self):
        super().setUp()
        self.k00 = Killmail(self.uk00)
        self.k30 = Killmail(self.uk30)

    def test_id(self):
        self.assertEqual(self.k00.id, 71443648, "The ID of the Killmail is wrong")
        self.assertEqual(self.k30.id, 71933840, "The ID of the Killmail is wrong")

    def test_time(self):
        self.assertEqual(self.k00.time, "2018-07-24T17:56:14Z", "The Time of the Killmail is wrong")
        self.assertEqual(self.k30.time, "2018-08-18T11:39:49Z", "The Time of the Killmail is wrong")

    def test_total_value(self):
        self.assertEqual(self.k00.total_value, 7521431.46, "The Total Value is wrong")
        self.assertEqual(self.k30.total_value, 227289291.33, "The Total Value is wrong")

    def test_attacker_is_npc(self):
        self.assertEqual(self.k00.attacker_is_npc, False, "The Attacker not an Npc")
        self.assertEqual(self.k30.attacker_is_npc, False, "The Attacker not an Npc")

    def test_attacker_is_awox(self):
        self.assertEqual(self.k00.attacker_is_awox, False, "The Attacker not an Awox")
        self.assertEqual(self.k30.attacker_is_awox, False, "The Attacker not an Awox")

    def test_attacker_is_solo(self):
        self.assertEqual(self.k00.attacker_is_solo, True, "The Attacker is Solo")
        self.assertEqual(self.k30.attacker_is_solo, False, "The Attacker is not Solo")

    def test_attacker_amount(self):
        self.assertEqual(self.k00.attacker_amount, 1, "There is only one Attacker")
        self.assertEqual(self.k30.attacker_amount, 2, "There are 2 Attackers")

    def test_victim_damage_taken(self):
        self.assertEqual(self.k00.victim_damage_taken, 4110, "Wrong damage")
        self.assertEqual(self.k30.victim_damage_taken, 1737, "Wrong damage")


class TestKillmailNames(Setup):

    def setUp(self):
        super().setUp()

        self.k00 = Killmail(self.uk00)

        self.k10 = Killmail(self.uk10)
        self.k11 = Killmail(self.uk11)
        self.k12 = Killmail(self.uk12)
        self.k13 = Killmail(self.uk13)
        self.k14 = Killmail(self.uk14)
        self.k15 = Killmail(self.uk15)
        self.k16 = Killmail(self.uk16)
        self.k17 = Killmail(self.uk17)
        self.k18 = Killmail(self.uk18)

        self.k20 = Killmail(self.uk20)
        self.k21 = Killmail(self.uk21)
        self.k22 = Killmail(self.uk22)
        self.k23 = Killmail(self.uk23)
        self.k24 = Killmail(self.uk24)
        self.k25 = Killmail(self.uk25)
        self.k26 = Killmail(self.uk26)
        self.k27 = Killmail(self.uk27)

        self.k30 = Killmail(self.uk30)
        self.k31 = Killmail(self.uk31)
        self.k32 = Killmail(self.uk32)
        self.k33 = Killmail(self.uk33)
        self.k34 = Killmail(self.uk34)
        self.k35 = Killmail(self.uk35)
        self.k36 = Killmail(self.uk36)
        self.k37 = Killmail(self.uk37)
        self.k38 = Killmail(self.uk38)
        self.k39 = Killmail(self.uk39)
        self.k40 = Killmail(self.uk40)
        self.k41 = Killmail(self.uk41)
        self.k42 = Killmail(self.uk42)
        self.k43 = Killmail(self.uk43)
        self.k44 = Killmail(self.uk44)
        self.k45 = Killmail(self.uk45)
        self.k46 = Killmail(self.uk46)

        self.k60 = Killmail(self.uk60)

    def test_solar_system_name(self):
        self.assertEqual(self.k00.solar_system_name, "DO6H-Q", "Wrong system")
        self.assertEqual(self.k30.solar_system_name, "Jita", "Wrong system")
        self.assertEqual(self.k60.solar_system_name, "", "Should return empty String")

    def test_victim_ship_name(self):
        pass

    def test_victim_name(self):
        pass

    def test_attacker_ship_name(self):
        pass

    def test_attacker_names(self):
        self.assertEqual(AttackerNameFetcher(self.uk18).getNames(), {"character": "", "corporation": "", "alliance": ""}, "Wrong dict")
        self.assertEqual(AttackerNameFetcher(self.uk10).getNames(), {"character": "", "corporation": ";NED-Clan;", "alliance": ";Goonswarm Federation;"}, "The returned Dict is wrong")
        self.assertEqual(AttackerNameFetcher(self.uk31).getNames(),
                     {"character": ";Ailiece Ardua;",
                      "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                      "alliance": ";Jita Holding Inc.;"},
                     "The returned Dict is wrong")
        self.assertEqual(AttackerNameFetcher(self.uk32).getNames(),
                         {"character": "",
                          "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                          "alliance": ";Jita Holding Inc.;"},
                         "The returned Dict is wrong")
        self.assertEqual(AttackerNameFetcher(self.uk12).getNames(),
                         {"character": ";Strife Senior;", "corporation": "", "alliance": ";Goonswarm Federation;"},
                         "The returned Dict is wrong")
        self.assertEqual(AttackerNameFetcher(self.uk14).getNames(),
                         {"character": ";Strife Senior;", "corporation": ";NED-Clan;", "alliance": ""},
                         "The returned Dict is wrong")
        self.assertEqual(AttackerNameFetcher(self.uk00).getNames(),
                         {"character": ";Strife Senior;", "corporation": ";NED-Clan;",
                          "alliance": ";Goonswarm Federation;"},
                         "The returned Dict is wrong")
        self.assertEqual(AttackerNameFetcher(self.uk30).getNames(),
                         {"character": ";Shotgun Pimp;Ailiece Ardua;",
                          "corporation": ";The Reappropriation Committee;HC - georgieboys;",
                          "alliance": ";Jita Holding Inc.;"},
                         "The returned Dict is wrong")

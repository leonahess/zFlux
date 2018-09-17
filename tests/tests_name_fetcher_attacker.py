from tests.setup import Setup
from src.name_fetcher_attacker import NameFetcherAttacker


class TestNameFetcherAttacker (Setup):

    def setUp(self):
        super().setUp()
        self.k00 = NameFetcherAttacker(self.uk00)
        self.k30 = NameFetcherAttacker(self.uk30)
        self.k70 = NameFetcherAttacker(self.uk70)

    def test_attacker_is_solo(self):
        self.assertEqual(False, self.k00.attacker_is_solo, "wrong bool")
        self.assertEqual(False, self.k30.attacker_is_solo, "wrong bool")
        self.assertEqual(False, self.k70.attacker_is_solo, "wrong bool")

    def test_attacker_is_npc(self):
        self.assertEqual(False, self.k00.attacker_is_npc, "wrong bool")
        self.assertEqual(False, self.k30.attacker_is_npc, "wrong bool")
        self.assertEqual(False, self.k70.attacker_is_npc, "wrong bool")

    def test_attacker_is_awox(self):
        self.assertEqual(False, self.k00.attacker_is_awox, "wrong  bool")
        self.assertEqual(False, self.k30.attacker_is_awox, "wrong  bool")
        self.assertEqual(False, self.k70.attacker_is_awox, "wrong  bool")

    def test_attacker_amount(self):
        self.assertEqual(1, self.k00.attacker_amount, "wrong int")
        self.assertEqual(2, self.k30.attacker_amount, "wrong int")
        self.assertEqual(2, self.k70.attacker_amount, "wrong int")

    def test_attacker_char_names(self):
        self.assertEqual(";Strife Senior;", self.k00.attacker_char_names, "wrong name")
        self.assertEqual(";Shotgun Pimp;Ailiece Ardua;", self.k30.attacker_char_names, "wron name")
        self.assertEqual(";VorSunder Vampyra;Jagreen Doshu;", self.k70.attacker_char_names, "wron name")

    def test_attacker_corp_names(self):
        self.assertEqual(";NED-Clan;", self.k00.attacker_corp_names, "wrong name")
        self.assertEqual(";The Reappropriation Committee;HC - georgieboys;", self.k30.attacker_corp_names, "wrong name")
        self.assertEqual(";Voracious Vikings of Valor;Old Rotten Tomatoes;", self.k70.attacker_corp_names, "wrong name")

    def test_attacker_alliance_names(self):
        self.assertEqual(";Goonswarm Federation;", self.k00.attacker_alliance_names, "wrong name")
        self.assertEqual(";Jita Holding Inc.;", self.k30.attacker_alliance_names, "wrong name")
        self.assertEqual("", self.k70.attacker_alliance_names, "wrong name")

    def test_attacker_ship_ids(self):
        self.assertEqual([605], self.k00.attacker_ship_ids, "wrong ids")
        self.assertEqual([29990], self.k30.attacker_ship_ids, "wrong ids")
        self.assertEqual([22456, 33470], self.k70.attacker_ship_ids, "wrong ids")

    def test_attacker_ship_names(self):
        self.assertEqual(";Heron;", self.k00.attacker_ship_names, "wrong names")
        self.assertEqual(";Loki;", self.k30.attacker_ship_names, "wrong names")
        self.assertEqual(";Sabre;Stratios;", self.k70.attacker_ship_names, "wrong names")

    def test_attacker_ship_group_ids(self):
        self.assertEqual(["25"], self.k00.attacker_ship_group_ids, "wrong ids")
        self.assertEqual(["963"], self.k30.attacker_ship_group_ids, "wrong ids")
        self.assertEqual(["541", "26"], self.k70.attacker_ship_group_ids, "wrong ids")

    def test_attacker_ship_group_names(self):
        self.assertEqual(";Frigate;", self.k00.attacker_ship_group_names, "wrong names")
        self.assertEqual(";Strategic Cruiser;", self.k30.attacker_ship_group_names, "wrong names")
        self.assertEqual(";Cruiser;Interdictor;", self.k70.attacker_ship_group_names, "wrong names")
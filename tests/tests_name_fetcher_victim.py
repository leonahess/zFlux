from tests.setup import Setup
from src.name_fetcher_victim import NameFetcherVictim


class TestNameFetcherVictim(Setup):

    def setUp(self):
        super().setUp()
        self.k00 = NameFetcherVictim(self.uk00)
        self.k30 = NameFetcherVictim(self.uk30)
        self.k70 = NameFetcherVictim(self.uk70)

    def test_victim_damage_taken(self):
        self.assertEqual(4110, self.k00.victim_damage_taken, "wrong int")
        self.assertEqual(1737, self.k30.victim_damage_taken, "wrong int")
        self.assertEqual(2087, self.k70.victim_damage_taken, "wrong int")

    def test_victim_char_id(self):
        self.assertEqual(2114300996, self.k00.victim_char_id, "wrong id")
        self.assertEqual(2113228085, self.k30.victim_char_id, "wrong id")
        self.assertEqual(2112516399, self.k70.victim_char_id, "wrong id")

    def test_victim_corp_id(self):
        self.assertEqual(98531953, self.k00.victim_corp_id, "wrong id")
        self.assertEqual(98446928, self.k30.victim_corp_id, "wrong id")
        self.assertEqual(1000180, self.k70.victim_corp_id, "wrong id")

    def test_victim_alliance_id(self):
        self.assertEqual(99007362, self.k00.victim_alliance_id, "wrong id")
        self.assertEqual(99003581, self.k30.victim_alliance_id, "wrong id")
        self.assertEqual("", self.k70.victim_alliance_id, "wrong id")

    def test_victim_char_name(self):
        self.assertEqual("Assassin Jx", self.k00.victim_char_name, "wrong name")
        self.assertEqual("Omae Kumiko", self.k30.victim_char_name, "wrong name")
        self.assertEqual("Dmitry Ismagilov", self.k70.victim_char_name, "wrong name")

    def test_victim_corp_name(self):
        self.assertEqual("Rainbow Pegasus Squadron", self.k00.victim_corp_name, "wrong name")
        self.assertEqual("Setcreasea Pallida Corporation", self.k30.victim_corp_name, "wrong name")
        self.assertEqual("State Protectorate", self.k70.victim_corp_name, "wrong name")

    def test_victim_alliance_name(self):
        self.assertEqual("Ranger Regiment", self.k00.victim_alliance_name, "wrong name")
        self.assertEqual("Fraternity.", self.k30.victim_alliance_name, "wrong name")
        self.assertEqual("", self.k70.victim_alliance_name, "wrong name")

    def test_victim_ship_id(self):
        self.assertEqual(32878, self.k00.victim_ship_id, "wrong id")
        self.assertEqual(33468, self.k30.victim_ship_id, "wrong id")
        self.assertEqual(33468, self.k70.victim_ship_id, "wrong id")

    def test_victim_ship_name(self):
        self.assertEqual("Talwar", self.k00.victim_ship_name, "wrong name")
        self.assertEqual("Astero", self.k30.victim_ship_name, "wrong name")
        self.assertEqual("Astero", self.k70.victim_ship_name, "wrong name")

    def test_victim_ship_group_id(self):
        self.assertEqual(420, self.k00.victim_ship_group_id, "wrong id")
        self.assertEqual(25, self.k30.victim_ship_group_id, "wrong id")
        self.assertEqual(25, self.k70.victim_ship_group_id, "wrong id")

    def test_victim_ship_group_name(self):
        self.assertEqual("Destroyer", self.k00.victim_ship_group_name, "wrong name")
        self.assertEqual("Frigate", self.k30.victim_ship_group_name, "wrong name")
        self.assertEqual("Frigate", self.k70.victim_ship_group_name, "wrong name")
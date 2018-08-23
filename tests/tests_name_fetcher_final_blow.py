from tests.setup import Setup
from name_fetcher_final_blow import NameFetcherFinalBlow


class TestNameFetcherFinalBlow (Setup):

    def setUp(self):
        super().setUp()
        self.k00 = NameFetcherFinalBlow(self.uk00)
        self.k30 = NameFetcherFinalBlow(self.uk30)
        self.k70 = NameFetcherFinalBlow(self.uk70)

    def test_final_blow_damage(self):
        self.assertEqual(4110, self.k00.final_blow_damage, "Wrong damage")
        self.assertEqual(778, self.k30.final_blow_damage, "wrong damage")
        self.assertEqual(1002, self.k70.final_blow_damage, "wrong damage")

    def test_final_blow_ship_id(self):
        self.assertEqual(605, self.k00.final_blow_ship_id, "Wrong ship id")
        self.assertEqual(29990, self.k30.final_blow_ship_id, "wrong ship id")
        self.assertEqual(33470, self.k70.final_blow_ship_id, "wrong ship id")

    def test_final_blow_ship_name(self):
        self.assertEqual("Heron", self.k00.final_blow_ship_name, "Wrong Ship Name")
        self.assertEqual("Loki", self.k30.final_blow_ship_name, "wrong ship name")
        self.assertEqual("Stratios", self.k70.final_blow_ship_name, "wrong ship name")

    def test_final_blow_ship_group_id(self):
        self.assertEqual("25", self.k00.final_blow_ship_group_id, "Wrong Group id")
        self.assertEqual("963", self.k30.final_blow_ship_group_id, "wrong group id")
        self.assertEqual("26", self.k70.final_blow_ship_group_id, "Wrong Group id")

    def test_final_blow_ship_group_name(self):
        self.assertEqual("Frigate", self.k00.final_blow_ship_group_name, "Wrong group name")
        self.assertEqual("Strategic Cruiser", self.k30.final_blow_ship_group_name, "wrong group name")
        self.assertEqual("Cruiser", self.k70.final_blow_ship_group_name, "Wrong group name")
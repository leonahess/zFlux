from tests.setup import Setup
from src.name_fetcher_geographic import NameFetcherGeographic


class TestNameFetcherGeographic(Setup):

    def setUp(self):
        super().setUp()
        self.k00 = NameFetcherGeographic(self.uk00)
        self.k30 = NameFetcherGeographic(self.uk30)
        self.k70 = NameFetcherGeographic(self.uk70)

    def test_solar_system_id(self):
        self.assertEqual(30003681, self.k00.solar_system_id, "wrong id")
        self.assertEqual(30000142, self.k30.solar_system_id, "wrong id")
        self.assertEqual(31000153, self.k70.solar_system_id, "wrong id")

    def test_solar_system_name(self):
        self.assertEqual("DO6H-Q", self.k00.solar_system_name, "wrong name")
        self.assertEqual("Jita", self.k30.solar_system_name, "wrong name")
        self.assertEqual("J113820", self.k70.solar_system_name, "wrong name")

    def test_solar_system_security(self):
        self.assertEqual(-0.3, self.k00.solar_system_security, "wrong float")
        self.assertEqual(0.9, self.k30.solar_system_security, "wrong float")
        self.assertEqual(-1.0, self.k70.solar_system_security, "wrong float")

    def test_solar_system_class(self):
        self.assertEqual("nullsec", self.k00.solar_system_class, "wrong name")
        self.assertEqual("highsec", self.k30.solar_system_class, "wrong name")
        self.assertEqual("wormhole", self.k70.solar_system_class, "wrong name")

    def test_region_id(self):
        self.assertEqual(10000046, self.k00.region_id, "wrong id")
        self.assertEqual(10000002, self.k30.region_id, "wrong id")
        self.assertEqual(11000002, self.k70.region_id, "wrong id")

    def test_region_name(self):
        self.assertEqual("Fade", self.k00.region_name, "wrong name")
        self.assertEqual("The Forge", self.k30.region_name, "wrong name")
        self.assertEqual("A-R00002", self.k70.region_name, "wrong name")

    def test_constellation_id(self):
        self.assertEqual(20000536, self.k00.constellation_id, "wrong id")
        self.assertEqual(20000020, self.k30.constellation_id, "wrong id")
        self.assertEqual(21000002, self.k70.constellation_id, "wrong id")

    def test_constellation_name(self):
        self.assertEqual("XFLN-F", self.k00.constellation_name, "wrong name")
        self.assertEqual("Kimotoro", self.k30.constellation_name, "wrong name")
        self.assertEqual("A-C00002", self.k70.constellation_name, "wrong name")

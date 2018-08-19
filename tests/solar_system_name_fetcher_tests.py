from tests.setup import Setup
from solar_system_name_fetcher import SolarSystemNameFetcher


class TestSolarSystemNameFetcher(Setup):

    def setUp(self):
        super().setUp()
        self.s00 = SolarSystemNameFetcher(self.uk00)
        self.s60 = SolarSystemNameFetcher(self.uk60)

    def test_get_names(self):
        self.assertEqual(self.s00.getNames(), "DO6H-Q", "Should return the right String")
        self.assertEqual(self.s60.getNames(), "", "Should return an empty string")

    def test_extract_names_from_dict(self):
        self.assertEqual(self.s00.extractNamesFromDict(self.s00.fetchNameWithId()), "DO6H-Q", "Should return the right String")
        self.assertEqual(self.s60.extractNamesFromDict(self.s60.fetchNameWithId()), "", "Should return an empty string")

    def test_generate_id_list(self):
        self.assertEqual(self.s00.generateIdList(), [30003681], "generateList() should return the correct list")
        self.assertEqual(self.s60.generateIdList(), [], "generateList() should return an empty List")

    def test_fetch_name_with_id(self):
        self.assertEqual(self.s00.fetchNameWithId(), [{"category": "solar_system", "id": 30003681, "name": "DO6H-Q"}], "fetchNameWithId() Should return the correct List")
        self.assertEqual(self.s60.fetchNameWithId(), [], "fetchNameWithId() should return an empty List")

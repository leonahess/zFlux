from tests.setup import Setup
from src.name_fetcher_attacker import NameFetcherAttacker


class TestNameFetcherAttacker (Setup):

    def setUp(self):
        super().setUp()
        self.k00 = NameFetcherAttacker(self.uk00)
        self.k30 = NameFetcherAttacker(self.uk30)
        self.k70 = NameFetcherAttacker(self.uk70)

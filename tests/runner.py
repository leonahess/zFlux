import unittest

# import test modules
from tests import tests_killmail2

from tests import name_fetcher_tests
from tests import attacker_name_fetcher_tests
from tests import victim_name_fetcher_tests
from tests import esi_call_tests
from tests import redisq_tests
from tests import influx_pusher_tests
from tests import ship_name_fetcher_tests
from tests import victim_ship_name_fetcher_tests
from tests import attacker_ship_name_fetcher_tests


def testSuite():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    suite.addTest(loader.loadTestsFromModule(tests_killmail2))

    return suite


if __name__ == "__main__":
    # initialize a runner, pass it the suite and run it
    mySuite = testSuite()
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(mySuite)

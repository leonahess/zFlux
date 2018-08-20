import unittest

# import test modules
from tests import killmail_tests
from tests import name_fetcher_tests
from tests import attacker_name_fetcher_tests
from tests import victim_name_fetcher_tests
from tests import solar_system_name_fetcher_tests
from tests import esi_call_tests
from tests import redisq_tests
from tests import influx_pusher_tests
from tests import main_tests
from tests import ship_name_fetcher_tests
from tests import victim_ship_name_fetcher_tests
from tests import attacker_ship_name_fetcher_tests


def testSuite():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    #suite.addTest(loader.loadTestsFromModule(killmail_tests))
    suite.addTest(loader.loadTestsFromModule(name_fetcher_tests))
    suite.addTest(loader.loadTestsFromModule(victim_name_fetcher_tests))
    suite.addTest(loader.loadTestsFromModule(attacker_name_fetcher_tests))
    suite.addTest(loader.loadTestsFromModule(esi_call_tests))
    suite.addTest(loader.loadTestsFromModule(solar_system_name_fetcher_tests))
    suite.addTest(loader.loadTestsFromModule(redisq_tests))
    suite.addTest(loader.loadTestsFromModule(influx_pusher_tests))
    suite.addTest(loader.loadTestsFromModule(main_tests))
    suite.addTest(loader.loadTestsFromModule(ship_name_fetcher_tests))
    suite.addTest(loader.loadTestsFromModule(attacker_ship_name_fetcher_tests))
    suite.addTest(loader.loadTestsFromModule(victim_ship_name_fetcher_tests))

    return suite


if __name__ == "__main__":
    # initialize a runner, pass it the suite and run it
    mySuite = testSuite()
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(mySuite)

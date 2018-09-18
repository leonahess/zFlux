import unittest

# import test modules
from tests import tests_killmail
from tests import tests_name_fetcher_final_blow
from tests import tests_name_fetcher_geographic
from tests import tests_name_fetcher_victim


def testSuite():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    suite.addTest(loader.loadTestsFromModule(tests_killmail))
    suite.addTest(loader.loadTestsFromModule(tests_name_fetcher_final_blow))
    suite.addTest(loader.loadTestsFromModule(tests_name_fetcher_geographic))
    suite.addTest(loader.loadTestsFromModule(tests_name_fetcher_victim))

    return suite


if __name__ == "__main__":
    # initialize a runner, pass it the suite and run it
    mySuite = testSuite()
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(mySuite)

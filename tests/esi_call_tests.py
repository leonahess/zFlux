import unittest

from src.esi_call import EsiCall


class TestEsiCall(unittest.TestCase):

    def setUp(self):
        self.l1 = []
        self.l2 = [99003006]
        self.l3 = [435128905194612105]

    def testEmpty(self):
        self.assertEqual(EsiCall.makeCall(EsiCall(), self.l1), [], "Did not return a empty list")

    def testCorrectId(self):
        self.assertEqual(EsiCall.makeCall(EsiCall(), self.l2), [{"category": "alliance", "id": 99003006, "name": "Brothers of Tangra"}])

    def testWrongId(self):
        self.assertEqual(EsiCall.makeCall(EsiCall(), self.l3), [], "Did not fail well on wrong ID")

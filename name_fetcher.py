from abc import ABC, abstractmethod
from esi_call import EsiCall


class NameFetcher(ABC):

    def __init__(self, unprocessed_killmail):
        self.unprocessed_killmail = unprocessed_killmail

    @staticmethod
    def makeCall(ids):
        return EsiCall.makeCall(ids)

    def fetchNameWithId(self):
        ids = self.generateIdList()

        if len(ids) < 1000 and len(ids) is not 0:
            names = self.makeCall(ids)
        else:
            names = []

        return names

    @abstractmethod
    def generateIdList(self):
        pass

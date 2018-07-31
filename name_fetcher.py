import logging
from abc import ABC, abstractmethod
from esi_call import EsiCall


class NameFetcher(ABC):
    """Abstrac Parent Class for the Different ID TO NAME stuff I have to do."""

    def __init__(self, unprocessed_killmail):
        self.unprocessed_killmail = unprocessed_killmail
        self.logger = logging.getLogger(__name__ + ".NameFetcher")

    @staticmethod
    def makeCall(ids):
        return EsiCall.makeCall(EsiCall(), ids)

    def fetchNameWithId(self):
        ids = self.generateIdList()

        self.logger.debug("Name Fetcher ids: {}".format(ids))

        if len(ids) < 1000 and len(ids) is not 0:
            names = self.makeCall(ids)
        else:
            names = []
        self.logger.debug("Names: {}".format(names))
        return names

    @abstractmethod
    def generateIdList(self):
        pass

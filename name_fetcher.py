import logging
from abc import ABC, abstractmethod
from esi_call import EsiCall


class NameFetcher(ABC):
    """Abstrac Parent Class for the Different ID TO NAME stuff I have to do."""

    def __init__(self, unprocessed_killmail):
        self.unprocessed_killmail = unprocessed_killmail
        self.logger = logging.getLogger(__name__ + ".NameFetcher")

    def getNames(self):
        names_dict = self.fetchNameWithId()
        names = self.extractNamesFromDict(names_dict)
        return names

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

    def extractNamesFromDict(self, names_dict):
        char_str = ";"
        corp_str = ";"
        alliance_str = ";"

        for entry in names_dict:
            if "name" in entry and "character" in entry["category"]:
                char_str = char_str + entry["name"] + ";"
            if "name" in entry and "corporation" in entry["category"]:
                corp_str = corp_str + entry["name"] + ";"
            if "name" in entry and "alliance" in entry["category"]:
                alliance_str = alliance_str + entry["name"] + ";"

        if char_str == ";":
            char_str = ""
        if corp_str == ";":
            corp_str = ""
        if alliance_str == ";":
            alliance_str = ""

        names = {"character": char_str, "corporation": corp_str, "alliance": alliance_str}

        return names

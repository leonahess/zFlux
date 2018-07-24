from abc import ABC, abstractmethod


class NameFetcher(ABC):

    def __init__(self, unprocessed_killmail):
        self.unprocessed_killmail = unprocessed_killmail

    @abstractmethod
    def fetchNameWithId(self):
        pass

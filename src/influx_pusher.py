import logging
from abc import abstractmethod, ABC
from influxdb import InfluxDBClient


class InfluxPusher(ABC):
    """Handles all things related to getting data ready for the database and moving said data to the database"""

    def __init__(self):
        """Connect to Database and check if database 'eve' exists, otherwise create one"""
        self.logger = logging.getLogger(__name__ + ".InfluxPusher")
        self.client = InfluxDBClient(host='localhost', port=8086, database='eve')
        database_list = self.client.get_list_database()
        eve_exists = False

        for s in range(0, len(database_list)):
            if database_list[s]['name'] == 'eve':
                eve_exists = True
        if not eve_exists:
            self.client.create_database('eve')

    @abstractmethod
    def assembleJsonBody(self, x):
        pass

    @abstractmethod
    def writeToDatabase(self, x):
        pass

from pymongo import MongoClient


class MongoPusher:

    def __init__(self, ip, port, database):
        self.client = MongoClient(ip, port)
        self.db = self.client[database]
        self.collection = self.db['killmails']

    def writeToDatabase(self, json):
        self.collection.insert_one(json)

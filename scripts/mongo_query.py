# Queries all entries from the mongoDB abd prints them

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['eve']
collection = db['killmails']

for x in collection.find():
    print(x)

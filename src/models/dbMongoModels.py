import pymongo
from config import databaseName, databaseURI


mongoClient = pymongo.MongoClient(databaseURI)
mongoDb = mongoClient[databaseName]
mongoCollection = mongoDb[databaseName]
dataTable = mongoDb.get_collection("data")
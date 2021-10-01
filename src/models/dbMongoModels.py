import pymongo
from config import databaseName, databaseURI


mongoClient = pymongo.MongoClient(databaseURI)
mongoDb = mongoClient[databaseName]
mongoCollection = mongoDb[databaseName]
nlpfDb = mongoClient.get_default_database()
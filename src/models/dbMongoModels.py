import pymongo
from config import databaseName, databaseURI, collectionLogs


mongoClient = pymongo.MongoClient(databaseURI)
mongoDb = mongoClient[databaseName]
mongoCollectionLogs = mongoClient[collectionLogs]
mongoCollection = mongoDb[databaseName]
dataTable = mongoDb.get_collection("data")
logsTable = mongoDb.get_collection("logs")

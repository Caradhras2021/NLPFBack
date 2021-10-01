# Database name
from pymongo import collection


databaseName = "APInlpf"

# Database password
mongodb_password="TxhE2sAnk4DEH!8"

# Database URI
databaseURI = 'mongodb+srv://caradhras:{}@apinlpf.elufi.mongodb.net/{}?retryWrites=true&w=majority'.format(mongodb_password, databaseName)

# Collection Name
collection_name = "data"
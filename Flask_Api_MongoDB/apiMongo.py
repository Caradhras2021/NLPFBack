from flask import Flask
from flask_mongoengine import MongoEngine
from api_constants import mongodb_password

db = MongoEngine()
app = Flask(__name__)
databaseName = "APInlpf"
databaseURI = 'mongodb+srv://caradhras:{}@apinlpf.elufi.mongodb.net/{}?retryWrites=true&w=majority'.format(mongodb_password, databaseName)
app.config["MONGO_HOST"] = databaseURI
db.init_app(app)


if __name__ == '__main__':
    app.run()
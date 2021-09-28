from logging import debug
from flask import Flask, json, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import *
from api_constants import mongodb_password
from request_api import *

app = Flask(__name__)
databaseName = "APInlpf"
databaseURI = 'mongodb+srv://caradhras:{}@apinlpf.elufi.mongodb.net/{}?retryWrites=true&w=majority'.format(mongodb_password, databaseName)
app.config["MONGODB_HOST"] = databaseURI
db = MongoEngine()
db.init_app(app)


class DateModel(db.Document):
    id = db.StringField(required=True)
    id_mutation = db.IntField()

    def to_json(self):
        return {
            "id": self.id,
            "id_mutation": self.id_mutation
        }


@app.route('/', methods=['GET'])
def get_date():
    dates = []
    for date in DateModel.objects:
        dates.append(date)
    return make_response(jsonify(dates), 200)

if __name__ == '__main__':
    app.run()(debug=True)
    


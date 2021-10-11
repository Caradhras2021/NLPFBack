from flask import Blueprint, render_template, request
from flask.helpers import make_response
from flask.json import jsonify
from models.dbMongoModels import dataTable
import json
from services.transactionService import transactionService

caradhras = Blueprint('caradhras', __name__)

@caradhras.route('/', methods=['GET', 'POST'])
def index():
    return render_template('./index.html')

@caradhras.route('/getOne', methods=['GET'])
def getOne():
    first_transaction = dataTable.find_one()

    return json.dumps(first_transaction)

### MAIN WITH FILTERS
@caradhras.route('/getTransaction/<page>/<pageSize>', methods=['POST'])
def getTransaction(page=1, pageSize=20):
    try:
        body = request.get_json()['data']
        # print('this is the bosy', body)
        res = transactionService(body, int(page), int(pageSize))
        # print(res)
        return res
    except:
        response = make_response(
                jsonify(
                    {"message": "can't filter, body not formatted correctly", "severity": "medium"}
                ),
                401,
            )
        response.headers["Content-Type"] = "application/json"
        return response

@caradhras.route('/getAll', methods=['GET'])
def getAll():
    transactions = dataTable.find()

    return json.dumps(transactions)

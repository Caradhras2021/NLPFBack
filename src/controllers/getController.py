from flask import Blueprint, render_template, request
from flask.helpers import make_response
from flask.json import jsonify
from models.dbMongoModels import dataTable
import json
from services.transactionService import transactionService, logsService, getLogsService

caradhras = Blueprint('caradhras', __name__)

@caradhras.route('/', methods=['GET', 'POST'])
def index():
    return render_template('./index.html')

@caradhras.route('/getOne', methods=['GET'])
def getOne():
    first_transaction = dataTable.find_one()

    return json.dumps(first_transaction)

@caradhras.route('/postLogs', methods=['POST'])
def postLogs():
    body = request.get_json()['data']
    return logsService(body['firstname'], body['lastname'], body['email_address'])

@caradhras.route('/getLogs', methods=['GET'])
def getLogs():
    try:
        return getLogsService()
    except:
        response = make_response(
                jsonify(
                    {"message": "can't access to logs history", "severity": "medium"}
                ),
                401,
            )
        response.headers["Content-Type"] = "application/json"
        return response
    

### MAIN WITH FILTERS
@caradhras.route('/getTransaction/<page>/<pageSize>', methods=['POST'])
def getTransaction(page=1, pageSize=20):
    try:
        body = request.get_json()['data']
        res = transactionService(body, int(page), int(pageSize))
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

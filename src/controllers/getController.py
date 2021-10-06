from flask import Blueprint, render_template, request
from flask.helpers import make_response
from flask.json import jsonify
from models.dbMongoModels import dataTable
from models.transactionModels import parse_json
from services.transactionService import getTransactionsService, transactionService

caradhras = Blueprint('caradhras', __name__)

@caradhras.route('/', methods=['GET', 'POST'])
def index():
    return render_template('./index.html')

@caradhras.route('/getOne', methods=['GET'])
def getOne():
    first_transaction = dataTable.find_one()

    return parse_json(first_transaction)

### MAIN WITH FILTERS
@caradhras.route('/getTransaction', methods=['GET'])
def getTransaction():
    try:
        body = request.get_json()
        res = transactionService(body)
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

    return parse_json(transactions)

@caradhras.route('/getTransactions', methods=['GET'])
def getTransactions():
    transactions = getTransactionsService()

    return parse_json(transactions)
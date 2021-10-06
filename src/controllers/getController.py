from flask import Blueprint, render_template, request
from flask.helpers import make_response
from flask.json import jsonify
from models.dbMongoModels import dataTable
from models.transactionModels import Transaction, parse_json
from models.dateModels import getDateModel
from services.transactionService import getTransactionsService, transactionService

caradhras = Blueprint('caradhras', __name__)

@caradhras.route('/', methods=['GET', 'POST'])
def index():
    data = request.data
    print('this is form', data)
    return render_template('./index.html')

def getOne():
    first_transaction = dataTable.find_one()

    return parse_json(first_transaction)

@caradhras.route('/getTransaction', methods=['GET'])
def getTransaction():
    try:
        body = request.get_json(force=True)
        blockSize = 20
        startIndex = 0
        transactionService(body, startIndex, blockSize)
        return "hello world"
    except:
        response = make_response(
                jsonify(
                    {"message": "can't filter, body not formatted correctly", "severity": "medium"}
                ),
                401,
            )
        response.headers["Content-Type"] = "application/json"
        return response


def getAll():
    transactions = dataTable.find()

    return parse_json(transactions)

def getTransactions():
    transactions = getTransactionsService()

    return parse_json(transactions)
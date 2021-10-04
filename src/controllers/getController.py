from flask import render_template
from models.dbMongoModels import dataTable
from models.transactionModels import parse_json
from models.dateModels import getDateModel
from services.transactionService import getTransactionService

def index():
    return render_template('./index.html')

def getOne():
    first_transaction = dataTable.find_one()

    return parse_json(first_transaction)

def getAll():
    transactions = dataTable.find()

    return parse_json(transactions)

def getTransactions():
    transactions = getTransactionService()

    return parse_json(transactions)
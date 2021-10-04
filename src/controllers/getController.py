from flask import render_template
from models.dbMongoModels import nlpfDb
import re
from models.transactionModels import parse_json

def index():
    return render_template('./index.html')

def getOne():
    dataTable = nlpfDb.get_collection("data")
    first_transaction = dataTable.find_one()

    return parse_json(first_transaction)

def getAll():
    dataTable = nlpfDb.get_collection("data")
    first_transaction = dataTable.find().limit(10)

    return parse_json(first_transaction)
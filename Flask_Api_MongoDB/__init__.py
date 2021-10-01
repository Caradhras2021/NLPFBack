from datetime import datetime
import os

import pymongo
# from flask_pymongo import PyMongo
# from pymongo.collection import Collection, ReturnDocument

import flask
from flask import Flask, request, url_for, jsonify, render_template

from environment import *

from model import Transaction
from helpers import *

# ------------------
my_client = pymongo.MongoClient(databaseURI)
my_db = my_client[databaseName]
my_collection = my_db[collection_name]
# ------------------

app = Flask(__name__)
app.config["MONGO_URI"] = databaseURI
# pymongo = PyMongo(app)



@app.route("/")
def root():
    return "Yep, you're in !"

@app.route("/hello")
def hello():
    return "Hello World !"

@app.route("/transaction/")
def one_transaction():
    """
    GET the first transaction.
    """

    first_transaction = my_collection.find_one()

    return parse_json(first_transaction)

@app.route("/transactions/")
def list_transactions():
    """
    GET a list of the first 10 transactions.
    """

    my_transactions = my_collection.find().limit(10)

    return parse_json(my_transactions)

if __name__ == '__main__':
    app.run()(debug=True)
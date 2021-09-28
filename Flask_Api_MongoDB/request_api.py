from flask import Flask, json, jsonify
from flask.helpers import make_response
from flask.wrappers import Response
from apiMongo import app

@app.route("/welcome")
def home():
    return "Hello World!"


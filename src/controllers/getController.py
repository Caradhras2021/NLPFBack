from flask import render_template
from models.dbMongoModels import nlpfDb
import re

def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower())

def index():
    return render_template('./index.html')


def getAll():
    recipes = nlpfDb.get_collection("data")
    recipes.create_index("slug", unique=True)
    for recipe in recipes.find():
        print(recipe["date_mutation"], slugify(recipe["date_mutation"]))
        recipes.update_one(
            {"_id": recipe["_id"]},
            {"$set": {"slug": slugify(recipe["date_mutation"])}},
        )
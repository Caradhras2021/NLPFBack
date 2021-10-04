from pydantic import BaseModel
from models.dbMongoModels import dataTable


# Catégorie : DATE
class Date(BaseModel):
    id_mutation: str
    date_mutation: str
    numero_disposition: int

def getDateModel():
    # transactions = dataTable.find({},{ "id_mutation": 1, "date_mutation": 1, "numero_disposition": 1 }).limit(10)
    transactions = dataTable.find({},{ "id_mutation": 1, "date_mutation": 1, "numero_disposition": 1 })

    return transactions
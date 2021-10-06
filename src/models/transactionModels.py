from models.dbMongoModels import dataTable
import json

mandatoryFileds = { "id_mutation": 1, "date_mutation": 1, "valeur_fonciere": 1, "adresse_numero": 1,
     "adresse_nom_voie": 1, "code_postal": 1, "nom_commune": 1, "longitude": 1, "latitude": 1, "surface_terrain": 1,
     "type_local": 1, "nombre_pieces_principales": 1, "lot1_surface_carrez": 1 }

def getTransactionModel():
    return dataTable.find({}, mandatoryFileds).limit(10)

def transactionModel(filters):
    arrayFilters = []
    for key, value in filters.items():
        if (str(value) != ""):
            arrayFilters.append({key: value})
    query = { "$and": arrayFilters }
    cursor = dataTable.find(query, mandatoryFileds)
    res = []
    for doc in cursor:
        doc.pop('_id')
        res.append(doc)
    response = json.dumps(res)
    return response

def to_bson(self):
    data = self.dict(by_alias=True, exclude_none=True)
    if data.get("_id") is None:
        data.pop("_id", None)
    return data

def parse_json(data):
    return dumps(data)
from models.dbMongoModels import dataTable
import json

mandatoryFileds = { "id_mutation": 1, "date_mutation": 1, "valeur_fonciere": 1, "adresse_numero": 1,
     "adresse_nom_voie": 1, "code_postal": 1, "nom_commune": 1, "longitude": 1, "latitude": 1, "surface_terrain": 1,
     "type_local": 1, "nombre_pieces_principales": 1, "lot1_surface_carrez": 1 }

def transactionModel(filters, pageNumber=0, pageSize=20):
    query = { "$and": filters }

    if (pageNumber == 0):
        cursor = dataTable.find(query, mandatoryFileds).limit(pageSize)
    else:
        cursor = dataTable.find(query, mandatoryFileds).skip(pageSize * (pageNumber - 1)).limit(pageSize)
    res = []
    for doc in cursor:
        doc.pop('_id')
        res.append(doc)
    response = json.dumps(res)
    return response

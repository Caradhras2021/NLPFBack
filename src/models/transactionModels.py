from models.dbMongoModels import dataTable
import json

mandatoryFields = { "id_mutation": 1, "date_mutation": 1, "valeur_fonciere": 1, "adresse_numero": 1,
     "adresse_nom_voie": 1, "code_postal": 1, "nom_commune": 1, "longitude": 1, "latitude": 1, "surface_terrain": 1,
     "type_local": 1, "nombre_pieces_principales": 1, "lot1_surface_carrez": 1 }

def transactionModel(filters, pageNumber=1, pageSize=20):
    query = { "$and": filters }
    if (pageNumber == 1):
        print("1. Page number : " + pageNumber + " and page size : " + pageSize)
        cursor = dataTable.find(query, mandatoryFields).limit(pageSize)
    else:
        skipValue = pageSize * (pageNumber) - 1
        cursor = dataTable.find(query, mandatoryFields).skip(skipValue).limit(pageNumber)
    res = []
    for doc in cursor:
        doc.pop('_id')
        res.append(doc)
    response = json.dumps(res)
    return response

from models.dbMongoModels import dataTable
import json

mandatoryFields = { "id_mutation": 1, "date_mutation": 1, "valeur_fonciere": 1, "adresse_numero": 1,
     "adresse_nom_voie": 1, "code_postal": 1, "nom_commune": 1, "longitude": 1, "latitude": 1, "surface_terrain": 1,
     "type_local": 1, "nombre_pieces_principales": 1, "lot1_surface_carrez": 1 }

def transactionModel(filters, surface, pageNumber=1, pageSize=20):
    if surface >= 0:
        surface_low = surface * 0.75
        surface_high = surface * 1.25
        query = { "$and": filters, "lot1_surface_carrez": { "$gte": surface_low, "$lte": surface_high } }
    else:
        query = { "$and": filters }

    if pageNumber == 0:
        pageNumber = 1
    if pageSize == 0:
        pageSize = 20

    skipValue = pageSize * ((pageNumber) - 1)
    cursor = dataTable.find(query, mandatoryFields).skip(skipValue).limit(pageSize)

    res = []
    for doc in cursor:
        doc.pop('_id')
        res.append(doc)
    response = json.dumps(res)
    
    return response

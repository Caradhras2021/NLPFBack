from models.dbMongoModels import dataTable, logsTable
import json
from datetime import datetime
from attrdict import AttrDict

mandatoryFields = { "id_mutation": 1, "date_mutation": 1, "valeur_fonciere": 1, "adresse_numero": 1,
     "adresse_nom_voie": 1, "code_postal": 1, "nom_commune": 1, "longitude": 1, "latitude": 1, "surface_terrain": 1,
     "type_local": 1, "nombre_pieces_principales": 1, "lot1_surface_carrez": 1 }

fieldsAverageSquarePrices = {"lot1_surface_carrez": 1, "valeur_fonciere": 1, "type_local": 1}

def jsonconverter(o):
    print(o)
    if isinstance(o, (datetime)):
        return o.__str__()
    return o

def getLogsModel():
    cursor = logsTable.find()
    res = []
    for doc in cursor:
        doc.pop('_id')
        res.append(doc)
    return json.dumps(res, default=jsonconverter)


def logsModel(firstname, lastname, emailAddress):
    now = datetime.now()
    try:
        logsTable.insert_one({'firstname': firstname, 'lastname': lastname, 'email_address': emailAddress, 'time': now})
        return "log inserted"
    except ValueError:
        return "can't add log into db."

def computeAverageSquarePrice(filters):
    query = { "$and": filters, "lot1_surface_carrez": { "$exists": True, "$not": {"$size": 0}},  "type_local": { "$exists": True, "$not": {"$size": 0}},
    "valeur_fonciere": { "$exists": True, "$not": {"$size": 0}}}
    cursor = dataTable.find(query, fieldsAverageSquarePrices).limit(5000)
    totalPriceApp = 0
    totalNbApp = 0
    totalPriceMais = 0
    totalNbMais = 0
    resApp = 0
    resMais = 0
    for doc in cursor:
        value = AttrDict(doc)
        tmpPriceApp = 0
        tmpPriceMais = 0
        try:
            if (str(value.type_local) == "Maison"):
                tmpPriceMais = int(value.valeur_fonciere) / int(value.lot1_surface_carrez)
                totalPriceMais += tmpPriceMais
                totalNbMais += 1
            elif (str(value.type_local) == "Appartement"):
                tmpPriceApp = int(value.valeur_fonciere) / int(value.lot1_surface_carrez)
                totalPriceApp += tmpPriceApp
                totalNbApp += 1
        except:
            continue
    if (totalNbApp > 0):
        resApp = totalPriceApp/totalNbApp
    elif (totalNbMais > 0):
        resMais = totalPriceMais/totalNbMais
    return (resApp, resMais)

# def checkFiltersAppMais(filters):
#     for (key) in filters:
#         value = AttrDict(key)
#         try:
#             if (str(value.type_local) == "Appartement" or str(value.type_local) == "Maison" or str(value.type_local) == "Both"):
#                 return True
#         except:
#             continue
#     return False

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
    (app, mais) = computeAverageSquarePrice(filters)
    obj = {"price_m2_appartement": app, "price_m2_maison": mais}
    res.append(obj)
    response = json.dumps(res)
    return response

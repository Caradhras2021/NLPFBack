from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional

from bson.json_util import dumps
from pydantic.json import ENCODERS_BY_TYPE

from models.dbMongoModels import dataTable

from models.objectid import PydanticObjectId
from models import dateModels, pricesModels, localisationsModels, parcellesModels, fieldModels, natureModels

class Transaction(BaseModel):
    # Should  PydanticObjectId be replace by ObjectId ?
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    date: dateModels.Date 
    prix: pricesModels.Prix
    localisation: localisationsModels.Localisation
    parcelle: parcellesModels.Parcelle
    terrain: fieldModels.Terrain
    nature: natureModels.Nature

def getTransactionModel():
    # transactions = dataTable.find({},{ "id_mutation": 1, "date_mutation": 1, "numero_disposition": 1 }).limit(10)
    transactions = dataTable.find({},{ "id_mutation": 1, "date_mutation": 1, "valeur_fonciere": 1, "adresse_numero": 1,
     "adresse_nom_voie": 1, "code_postal": 1, "nom_commune": 1, "longitude": 1, "latitude": 1, "surface_terrain": 1,
     "type_local": 1, "nombre_pieces_principales": 1, "lot1_surface_carrez": 1 }).limit(10)

    return transactions

def to_json(self):
    return jsonable_encoder(self, exclude_none=True)

def to_bson(self):
    data = self.dict(by_alias=True, exclude_none=True)
    if data.get("_id") is None:
        data.pop("_id", None)
    return data

def parse_json(data):
    return dumps(data)
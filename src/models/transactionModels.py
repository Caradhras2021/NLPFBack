from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional

from bson.json_util import dumps
from pydantic.json import ENCODERS_BY_TYPE

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

def to_json(self):
    return jsonable_encoder(self, exclude_none=True)

def to_bson(self):
    data = self.dict(by_alias=True, exclude_none=True)
    if data.get("_id") is None:
        data.pop("_id", None)
    return data

def parse_json(data):
    return dumps(data)
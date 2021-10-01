import os
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from bson.json_util import dumps
from typing import Optional
from objectIdHelper import PydanticObjectId
from models import dateModels, fieldModels, localisationsModels, natureModels, parcellesModels, pricesModels

class Transaction(BaseModel):
    # Should  PydanticObjectId be replace by ObjectId ?
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    date: dateModels
    prix: pricesModels
    localisation: localisationsModels
    parcelle: parcellesModels
    terrain: fieldModels
    nature: natureModels

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
    
    def parse_json(data):
        return dumps(data)
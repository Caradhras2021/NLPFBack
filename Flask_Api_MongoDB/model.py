# FastAPI's jsonable_encoder handles converting various non-JSON types,
# such as datetime between JSON types and native Python types.
from fastapi.encoders import jsonable_encoder

# Pydantic, and Python's built-in typing are used to define a schema
# that defines the structure and types of the different objects stored
# in the recipes collection, and managed by this API.
from pydantic import BaseModel, Field
from typing import List, Optional, Union
from datetime import datetime

from objectid import PydanticObjectId


# Catégorie : DATE
class Date(BaseModel):
    id_mutation: str
    date_mutation: str
    numero_disposition: int

# Catégorie : PRIX
class Prix(BaseModel):
    valeur_fonciere: int

# Catégorie : LOCALISATION
class Localisation(BaseModel):
    adresse_numero: Optional[str]
    adresse_suffixe: Optional[str]
    adresse_nom_voie: Optional[str]
    adresse_code_voie: Optional[str]
    code_postal: Optional[str]
    code_commune: Optional[str]
    nom_commune: Optional[str]
    code_departement: Optional[str]
    ancien_code_commune: Optional[str]
    ancien_nom_commune: Optional[str]
    id_parcelle: Optional[str]
    ancien_id_parcelle: Optional[str]
    longitude: Optional[str]
    latitude: Optional[str]

# Catégorie : PARCELLE_HABITABLE
class Parcelle(BaseModel):
    numero_volume: Optional[str]
    lot1_numero: Optional[str]
    lot1_surface_carrez: Optional[str]
    lot2_numero: Optional[str]
    lot2_surface_carrez: Optional[str]
    lot3_numero: Optional[str]
    lot3_surface_carrez: Optional[str]
    lot4_numero: Optional[str]
    lot4_surface_carrez: Optional[str]
    lot5_numero: Optional[str]
    lot5_surface_carrez: Optional[str]

# Catégorie : TERRAIN
class Terrain(BaseModel):
    nombre_lots: Optional[str]
    type_local: Optional[str]
    surface_reelle_bati: Optional[str]
    nombre_pieces_principales: Optional[str]
    surface_terrain: Optional[str]

# Catégorie : NATURE
class Nature(BaseModel):
    code_type_local: Optional[str]
    code_nature_culture: Optional[str]
    nature_culture: Optional[str]
    code_nature_culture_speciale: Optional[str]
    nature_culture_speciale: Optional[str]

class Transaction(BaseModel):
    # Should  PydanticObjectId be replace by ObjectId ?
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    date: Date
    prix: Prix
    localisation: Localisation
    parcelle: Parcelle
    terrain: Terrain
    nature: Nature
    # slug: str
    # name: str
    # ingredients: List[Ingredient]
    # instructions: List[str]
    # date_added: Optional[datetime]
    # date_updated: Optional[datetime]


    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
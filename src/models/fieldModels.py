from pydantic import BaseModel
from typing import Optional

# Catégorie : TERRAIN
class Terrain(BaseModel):
    nombre_lots: Optional[str]
    type_local: Optional[str]
    surface_reelle_bati: Optional[str]
    nombre_pieces_principales: Optional[str]
    surface_terrain: Optional[str]
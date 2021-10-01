from pydantic import BaseModel
from typing import Optional

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
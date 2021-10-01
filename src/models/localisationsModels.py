from pydantic import BaseModel
from typing import Optional

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
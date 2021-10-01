from pydantic import BaseModel
from typing import Optional


# Catégorie : NATURE
class Nature(BaseModel):
    code_type_local: Optional[str]
    code_nature_culture: Optional[str]
    nature_culture: Optional[str]
    code_nature_culture_speciale: Optional[str]
    nature_culture_speciale: Optional[str]
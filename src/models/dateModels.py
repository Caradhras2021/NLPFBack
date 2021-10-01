from pydantic import BaseModel

# Catégorie : DATE
class Date(BaseModel):
    id_mutation: str
    date_mutation: str
    numero_disposition: int
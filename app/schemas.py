from pydantic import BaseModel
from typing import List, Optional

class ClientSchema(BaseModel):
    client_id: int
    nom: str
    email: str
    ville: str
    tranche_age: Optional[str] = None

    class Config:
        from_attributes = True

class SalesByCitySchema(BaseModel):
    ville: str
    nb_ventes: int
    total_ttc: float

class ClientListResponse(BaseModel):
    count: int
    data: List[ClientSchema]

class SalesByCityResponse(BaseModel):
    data: List[SalesByCitySchema]
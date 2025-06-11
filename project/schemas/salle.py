from pydantic import BaseModel, Field

class SchemaSalle(BaseModel):
    id_salle: int = Field(...)
    nom: str = Field(...)
    capacite: int = Field(...)
    localisation: str
    actif: bool = Field(True)
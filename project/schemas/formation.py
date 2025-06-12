from pydantic import BaseModel, Field


class SchemaFormation(BaseModel):
    id_formation: int = Field(...)
    libelle: str = Field(...)

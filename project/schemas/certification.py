from pydantic import BaseModel, Field


class SchemaCertification(BaseModel):
    id_certification: int = Field(...)
    libelle: str = Field(...)

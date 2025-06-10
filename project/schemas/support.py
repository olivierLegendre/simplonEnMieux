from enum import Enum
from datetime import date
from pydantic import Field
from schemas.utilisateur import SchemaUtilisateur

class Poste(Enum):
    CDP = 'CDP' # Chef de projet
    RESP_P = 'RESP_P' # Responsable pédagogique

class SchemaSupport(SchemaUtilisateur):
    id_apprenant: int = Field(...)
    poste: Poste = Field(...)
    date_prise_fonction: date = Field(...)
    responsabilites: dict | None
from enum import Enum
from datetime import date
from pydantic import Field
from schemas.utilisateur import SchemaUtilisateur, SchemaUtilisateurListeBase

class Poste(Enum):
    CDP = 'CDP' # Chef de projet
    RESP_P = 'RESP_P' # Responsable pédagogique

class SchemaSupport(SchemaUtilisateur):
    poste: Poste = Field(...)
    date_prise_fonction: date = Field(...)
    responsabilites: dict | None

class SchemaSupportListeBase(SchemaUtilisateurListeBase):
    poste: Poste = Field(...)
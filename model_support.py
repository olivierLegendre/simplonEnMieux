from enum import Enum
from datetime import date
from pydantic import Field
from model_utilisateur import Utilisateur, UtilisateurListeBase

class Poste(Enum):
    CDP = 1 # Chef de projet
    RESP_P = 2 # Responsable pédagogique

class Support(Utilisateur):
    poste: Poste = Field(...)
    date_prise_fonction: date = Field(...)
    responsabilites: dict | None

class SupportListeBase(UtilisateurListeBase):
    poste: Poste = Field(...)
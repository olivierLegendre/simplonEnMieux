from enum import Enum
from datetime import datetime
from pydantic import Field
from schemas.schema_utilisateur import Utilisateur, UtilisateurListeBase

class NiveauAcces(Enum):
    ADMIN_STANDART = 'STD'
    SUPER_ADMIN = 'SUP'

class Admin(Utilisateur):
    niveau_acces: NiveauAcces = Field(...)
    date_promotion: datetime = Field(...)

class AdminListeBase(UtilisateurListeBase):
    niveau_acces: NiveauAcces = Field(...)
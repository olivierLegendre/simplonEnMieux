from enum import Enum
from datetime import datetime
from pydantic import Field
from schemas.utilisateur import SchemaUtilisateur, SchemaUtilisateurListeBase

class NiveauAcces(Enum):
    ADMIN_STANDART = 'STD'
    SUPER_ADMIN = 'SUP'

class SchemaAdmin(SchemaUtilisateur):
    id_admin: int = Field(...)
    niveau_acces: NiveauAcces = Field(...)
    date_promotion: datetime = Field(...)

class SchemaAdminListeBase(SchemaUtilisateurListeBase):
    id_admin: int = Field(...)
    niveau_acces: NiveauAcces = Field(...)
from enum import Enum
from datetime import datetime
from pydantic import Field
from schemas.schema_utilisateur import SchemaUtilisateur, SchemaUtilisateurListeBase

class NiveauAcces(Enum):
    ADMIN_STANDART = 'STD'
    SUPER_ADMIN = 'SUP'

class SchemaAdmin(SchemaUtilisateur):
    niveau_acces: NiveauAcces = Field(...)
    date_promotion: datetime = Field(...)

class SchemaAdminListeBase(SchemaUtilisateurListeBase):
    niveau_acces: NiveauAcces = Field(...)
from enum import Enum
from datetime import date
from pydantic import Field
from schemas.utilisateur import SchemaUtilisateur, SchemaUtilisateurListeBase

class NiveauEtude(Enum):
    INFERIEUR_BAC = 'INF'
    BAC = 'BAC'
    BAC_1 = 'BAC_1'
    BAC_2 = 'BAC_2'
    BAC_3 = 'BAC_3'
    BAC_4 = 'BAC_4'
    BAC_5 = 'BAC_5'
    SUPERIEUR = 'SUP'

class SchemaApprenant(SchemaUtilisateur):
    id_apprenant: int = Field(...)
    date_naissance: date = Field(...)
    date_inscription: date = Field(...)
    niveau_etude: NiveauEtude = Field(...)
    commentaire: str | None

class SchemaApprenantListeBase(SchemaUtilisateurListeBase):
    id_apprenant: int = Field(...)
    date_inscription: date = Field(...)
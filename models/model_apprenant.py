from enum import Enum
from datetime import date
from pydantic import Field
from model_utilisateur import Utilisateur, UtilisateurListeBase

class NiveauEtude(Enum):
    INFERIEUR_BAC = 'INF'
    BAC = 'BAC'
    BAC_1 = 'BAC_1'
    BAC_2 = 'BAC_2'
    BAC_3 = 'BAC_3'
    BAC_4 = 'BAC_4'
    BAC_5 = 'BAC_5'
    SUPERIEUR = 'SUP'

class Apprenant(Utilisateur):
    date_naissance: date = Field(...)
    date_inscription: date = Field(...)
    niveau_etude: NiveauEtude = Field(...)
    commentaire: str | None

class ApprenantListeBase(UtilisateurListeBase):
    date_inscription: date = Field(...)
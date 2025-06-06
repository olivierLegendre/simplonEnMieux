from enum import Enum
from datetime import date
from pydantic import Field
from model_utilisateur import Utilisateur, UtilisateurListeBase

class NiveauEtude(Enum):
    INFERIEUR_BAC = 1
    BAC = 2
    BAC_2 = 3
    BAC_3 = 4
    BAC_4 = 5
    BAC_5 = 6
    SUPERIEUR = 7

class Apprenant(Utilisateur):
    date_naissance: date = Field(...)
    date_inscription: date = Field(...)
    niveau_etude: NiveauEtude = Field(...)
    commentaire: str | None

class ApprenantListeBase(UtilisateurListeBase):
    date_inscription: date = Field(...)
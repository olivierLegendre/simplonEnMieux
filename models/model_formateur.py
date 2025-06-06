from datetime import date
from pydantic import Field
from model_utilisateur import Utilisateur, UtilisateurListeBase

class Formateur(Utilisateur):
    specialites: str
    date_embauche: date = Field(...)
    taux_horaire: float
    bio: str | None

class FormateurListeBase(UtilisateurListeBase):
    pass
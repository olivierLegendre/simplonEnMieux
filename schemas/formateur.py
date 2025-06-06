from datetime import date
from pydantic import Field
from schemas.utilisateur import SchemaUtilisateur, SchemaUtilisateurListeBase

class SchemaFormateur(SchemaUtilisateur):
    id_apprennant: int = Field(...)
    specialites: str
    date_embauche: date = Field(...)
    taux_horaire: float
    bio: str | None

class SchemaFormateurListeBase(SchemaUtilisateurListeBase):
    id_apprenant: int = Field(...)
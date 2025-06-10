from datetime import date
from pydantic import Field
from .utilisateur import SchemaUtilisateur, SchemaUtilisateurCreation

class SchemaFormateur(SchemaUtilisateur):
    id_apprennant: int = Field(...)
    specialites: str
    date_embauche: date = Field(...)
    taux_horaire: float
    bio: str | None

class SchemaFormateurCreation(SchemaUtilisateurCreation):
    pass
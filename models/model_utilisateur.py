from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

class Utilisateur(BaseModel):
    id: int = Field(...)
    nom: str = Field(..., max_length=50)
    prenom: str = Field(..., max_length=50)
    email: EmailStr
    date_creation: datetime = Field(...)
    telephone: str | None = Field(None, max_length=17)
    login: str = Field(..., max_length=10)
    mdp: str = Field(..., max_length=100)

class UtilisateurListeBase(BaseModel):
    id: int = Field(...)
    nom: str = Field(..., max_length=50)
    prenom: str = Field(..., max_length=50)
    email: EmailStr

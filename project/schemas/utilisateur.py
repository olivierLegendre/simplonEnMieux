from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

class SchemaUtilisateur(BaseModel):
    nom: str = Field(..., max_length=50)
    prenom: str = Field(..., max_length=50)
    email: EmailStr
    date_creation: datetime = Field(...)
    telephone: str | None = Field(None, max_length=17)
    login: str = Field(..., max_length=10)
    mdp: str = Field(..., max_length=100)

class SchemaUtilisateurCreation(BaseModel):
    nom: str = Field(..., max_length=50)
    prenom: str = Field(..., max_length=50)
    email: EmailStr
    login: str = Field(..., max_length=10)
    mdp: str = Field(..., max_length=256)

class SchemaUtilisateurMaj(BaseModel):
    nom: str = Field(..., max_length=50)
    prenom: str = Field(..., max_length=50)
    telephone: str | None = Field(None, max_length=17)
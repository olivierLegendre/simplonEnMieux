from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ModeleUtilisateur(Base):
    nom = Column(String)
    prenom = Column(String)
    email = Column(String)
    date_creation = Column(DateTime)
    telephone = Column(String)
    login = Column(String)
    mdp = Column(String)

class ModeleUtilisateurListeBase(Base):
    nom = Column(String)
    prenom = Column(String)
    email = Column(String)
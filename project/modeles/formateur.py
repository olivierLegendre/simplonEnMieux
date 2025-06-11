from sqlalchemy import Column, Integer, String, Date, Float, Text
#from sqlalchemy.ext.declarative import declarative_base
from .utilisateur import ModeleUtilisateur#, ModeleUtilisateurListeBase
from .. import db
from ..schemas.formateur import SchemaFormateur, SchemaFormateurCreation
#Base = declarative_base()

class ModeleFormateur(ModeleUtilisateur):
    __tablename__ = 'formateur'
    # __table_args__ = {'extend_existing': True}
    id_formateur = Column(Integer, primary_key=True)
    specialites = Column(String)
    date_embauche = Column(Date)
    taux_horaire = Column(Float)
    bio = Column(Text)

def creation_Formateur(**kwargs):
    schema = SchemaFormateurCreation(**kwargs)
    modele = ModeleFormateur(**schema.model_dump())
    db.session.add(modele)
    return modele

def maj_Formateur(**kwargs):
    schema = SchemaFormateur(**kwargs)
    modele = ModeleFormateur(**schema.model_dump())
    db.session.add(modele)
    return modele
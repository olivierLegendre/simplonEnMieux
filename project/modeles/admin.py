from sqlalchemy import Column, Integer, Enum, Date
#from sqlalchemy.ext.declarative import declarative_base
from .utilisateur import ModeleUtilisateur#, ModeleUtilisateurListeBase
from .. import db
from ..schemas.admin import SchemaAdmin, SchemaAdminCreation

#Base = declarative_base()

class ModeleAdmin(ModeleUtilisateur):
    __tablename__ = 'admin'
    id_admin = Column(Integer, primary_key=True)
    niveau_acces = Column(Enum)
    date_promotion = Column(Date)

def creation_Admin(**kwargs):
    schema = SchemaAdminCreation(**kwargs)
    modele = ModeleAdmin(**schema.model_dump())
    db.session.add(modele)
    return modele

def maj_Admin(**kwargs):
    schema = SchemaAdmin(**kwargs)
    modele = ModeleAdmin(**schema.model_dump())
    db.session.add(modele)
    return modele
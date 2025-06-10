from sqlalchemy import Column, Integer, Enum, Date, JSON
#from sqlalchemy.ext.declarative import declarative_base
from .utilisateur import ModeleUtilisateur#, ModeleUtilisateurListeBase
from .. import db
from ..schemas.support import SchemaSupport, SchemaSupportCreation

#Base = declarative_base()

class ModeleSupport(ModeleUtilisateur):
    __tablename__ = 'admin'
    id_support = Column(Integer, primary_key=True)
    poste = Column(Enum)
    date_prise_fonction = Column(Date)
    responsabilites = Column(JSON)

def creation_Support(**kwargs):
    schema = SchemaSupportCreation(**kwargs)
    modele = ModeleSupport(**schema.model_dump())
    db.session.add(modele)
    return modele

def maj_Support(**kwargs):
    schema = SchemaSupport(**kwargs)
    modele = ModeleSupport(**schema.model_dump())
    db.session.add(modele)
    return modele
from sqlalchemy import Column, String, SmallInteger, Boolean
from .. import db
from ..schemas.salle import SchemaSalle #, SchemaSalleCreation

class ModeleSalle(db.Model):
    __tablename__ = 'salle'
    id_salle = Column(SmallInteger, primary_key=True)
    nom = Column(String)
    capacite = Column(SmallInteger)
    localisation = Column(String)
    actif = Column(Boolean)

    def get_id(self):
        return self.id_salle

def creation_salle(**kwargs):
    schema = SchemaSalleCreation(**kwargs)
    modele = ModeleSalle(**schema.model_dump())
    db.session.add(modele)
    return modele

def maj_salle(**kwargs):
    schema = SchemaSalle(**kwargs)
    modele = ModeleSalle(**schema.model_dump())
    db.session.add(modele)
    return modele
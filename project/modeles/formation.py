from sqlalchemy import Column, String, SmallInteger
from .. import db
from ..schemas.formation import SchemaFormation, SchemaFormationCreation

class ModeleFormation(db.Model):
    __tablename__ = 'formation'
    id_formation = Column(SmallInteger, primary_key=True)
    libelle = Column(String)

    def get_id(self):
        return self.id_formation

def creation_formation(**kwargs):
    schema = SchemaFormationCreation(**kwargs)
    modele = ModeleFormation(**schema.model_dump())
    db.session.add(modele)
    return modele

def maj_formation(**kwargs):
    schema = SchemaFormation(**kwargs)
    modele = ModeleFormation(**schema.model_dump())
    db.session.add(modele)
    return modele
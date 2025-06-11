from sqlalchemy import Column, Integer, Enum, Date
from .utilisateur import ModeleUtilisateur#, ModeleUtilisateurListeBase
from .. import db
from ..schemas.admin import SchemaAdmin, SchemaAdminCreation

class ModeleAdmin(ModeleUtilisateur):
    __tablename__ = 'admin'
    id_admin = Column(Integer, primary_key=True)
    niveau_acces = Column(Enum)
    date_promotion = Column(Date)

    def get_id(self):
        return self.id_admin

def creation_admin(**kwargs):
    schema = SchemaAdminCreation(**kwargs)
    modele = ModeleAdmin(**schema.model_dump())
    db.session.add(modele)
    return modele

def maj_admin(**kwargs):
    schema = SchemaAdmin(**kwargs)
    modele = ModeleAdmin(**schema.model_dump())
    db.session.add(modele)
    return modele
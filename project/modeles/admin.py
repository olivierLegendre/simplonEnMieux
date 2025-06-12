from sqlalchemy import Column, Integer, Enum, Date
from .utilisateur import ModeleUtilisateur
from .. import db
from ..schemas.admin import SchemaAdmin, SchemaAdminCreation


class ModeleAdmin(ModeleUtilisateur):
    __tablename__ = "admin"
    id_admin = Column(Integer, primary_key=True)
    niveau_acces = Column(Enum)
    date_promotion = Column(Date)

    def get_id(self) -> int:
        return self.id_admin


def creation_admin(**kwargs) -> ModeleAdmin:
    schema = SchemaAdminCreation(**kwargs)
    modele = ModeleAdmin(**schema.model_dump())
    db.session.add(modele)
    return modele


def maj_admin(**kwargs) -> ModeleAdmin:
    schema = SchemaAdmin(**kwargs)
    modele = ModeleAdmin(**schema.model_dump())
    db.session.add(modele)
    return modele

from sqlalchemy import Column, Integer, Enum, Date, JSON
from .utilisateur import ModeleUtilisateur
from .. import db
from ..schemas.support import SchemaSupport, SchemaSupportCreation, Poste


class ModeleSupport(ModeleUtilisateur):
    __tablename__ = "support"
    id_support = Column(Integer, primary_key=True)
    poste = Column(Enum(Poste))
    date_prise_fonction = Column(Date)
    responsabilites = Column(JSON)

    def get_id(self) -> int:
        return self.id_support


def creation_support(**kwargs) -> ModeleSupport:
    schema = SchemaSupportCreation(**kwargs)
    modele = ModeleSupport(**schema.model_dump())
    db.session.add(modele)
    return modele


def maj_support(**kwargs) -> ModeleSupport:
    schema = SchemaSupport(**kwargs)
    modele = ModeleSupport(**schema.model_dump())
    db.session.add(modele)
    return modele

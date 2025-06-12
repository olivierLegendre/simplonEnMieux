from sqlalchemy import Column, Integer, String, Date, Float, Text
from .utilisateur import ModeleUtilisateur
from .. import db
from ..schemas.formateur import SchemaFormateur, SchemaFormateurCreation


class ModeleFormateur(ModeleUtilisateur):
    __tablename__ = "formateur"
    id_formateur = Column(Integer, primary_key=True)
    specialites = Column(String)
    date_embauche = Column(Date)
    taux_horaire = Column(Float)
    bio = Column(Text)

    def get_id(self) -> int:
        return self.id_formateur


def creation_formateur(**kwargs) -> ModeleFormateur:
    schema = SchemaFormateurCreation(**kwargs)
    modele = ModeleFormateur(**schema.model_dump())
    db.session.add(modele)
    return modele


def maj_formateur(**kwargs) -> ModeleFormateur:
    schema = SchemaFormateur(**kwargs)
    modele = ModeleFormateur(**schema.model_dump())
    db.session.add(modele)
    return modele

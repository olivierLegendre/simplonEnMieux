from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    Date,
    Enum,
    Text,
    String,
    SmallInteger,
)
from sqlalchemy.orm import relationship
from .. import db

from .utilisateur import ModeleUtilisateur
from ..schemas.apprenant import SchemaApprenantCreation, SchemaApprenantMaj, NiveauEtude
from ..schemas.certification import SchemaCertification

apprenant_certification = Table(
    "apprenant_certification",
    db.metadata,
    Column("id_apprenant", ForeignKey("apprenant.id_apprenant"), primary_key=True),
    Column(
        "id_certification",
        ForeignKey("certification.id_certification"),
        primary_key=True,
    ),
)


class ModeleApprenant(ModeleUtilisateur):
    __tablename__ = "apprenant"
    id_apprenant = Column(Integer, primary_key=True)
    date_naissance = Column(Date)
    date_inscription = Column(Date)
    niveau_etude = Column(Enum(NiveauEtude), nullable=True)
    commentaire = Column(Text)
    certifications = relationship(
        "ModeleCertification",
        secondary=apprenant_certification,
        back_populates="apprenants",
    )

    def get_id(self) -> int:
        return self.id_apprenant


def creation_apprenant(**kwargs) -> ModeleApprenant:
    schema = SchemaApprenantCreation(**kwargs)
    modele = ModeleApprenant(**schema.model_dump())
    db.session.add(modele)
    return modele


def maj_apprenant(modele_existant: ModeleApprenant, **kwargs) -> bool:
    schema = SchemaApprenantMaj(**kwargs)
    for champ, valeur in schema.__dict__.items():
        setattr(modele_existant, champ, valeur)
    return schema is not None


class ModeleCertification(db.Model):
    __tablename__ = "certification"
    id_certification = Column(SmallInteger, primary_key=True)
    libelle = Column(String)
    apprenants = relationship(
        "ModeleApprenant",
        secondary=apprenant_certification,
        back_populates="certifications",
    )

    def get_id(self) -> int:
        return self.id_certification


def creation_certification(**kwargs) -> ModeleCertification:
    schema = SchemaCertification(**kwargs)
    modele = ModeleCertification(**schema.model_dump())
    db.session.add(modele)
    return modele


def maj_certification(modele_existant: ModeleCertification, **kwargs) -> bool:
    schema = SchemaCertification(**kwargs)
    for champ, valeur in schema.__dict__.items():
        setattr(modele_existant, champ, valeur)
    return schema is not None

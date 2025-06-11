from sqlalchemy import Column, Integer, Enum, Date, Text
#from sqlalchemy.ext.declarative import declarative_base
from .utilisateur import ModeleUtilisateur#, ModeleUtilisateurListeBase
from ..schemas.apprenant import SchemaApprenant, SchemaApprenantCreation
from .. import db
#Base = declarative_base()

class ModeleApprenant(ModeleUtilisateur):
    __tablename__ = 'apprenant'
    # __table_args__ = {'extend_existing': True}
    id_apprenant = Column(Integer, primary_key=True)
    date_naissance = Column(Date)
    date_inscription = Column(Date)
    niveau_etude = Column(Enum)
    commentaire = Column(Text)
    
    def get_id(self):
        return self.id_apprenant
    
def creation_Apprenant(**kwargs):
    schema = SchemaApprenantCreation(**kwargs)
    modele = ModeleApprenant(**schema.model_dump())
    db.session.add(modele)
    return modele

def maj_Apprenant(**kwargs):
    schema = SchemaApprenant(**kwargs)
    modele = ModeleApprenant(**schema.model_dump())
    db.session.add(modele)
    return modele
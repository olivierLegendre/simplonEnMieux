from sqlalchemy import Column, Integer, Enum, Date
#from sqlalchemy.ext.declarative import declarative_base
from .utilisateur import ModeleUtilisateur#, ModeleUtilisateurListeBase

#Base = declarative_base()

class ModeleAdmin(ModeleUtilisateur):
    __tablename__ = 'admin'
    id_admin = Column(Integer, primary_key=True)
    niveau_acces = Column(Enum)
    date_promotion = Column(Date)
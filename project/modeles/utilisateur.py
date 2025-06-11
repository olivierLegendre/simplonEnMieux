from sqlalchemy import Column, String, DateTime, inspect
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from .. import db

class ModeleUtilisateur(UserMixin, db.Model):
    nom = Column(String)
    prenom = Column(String)
    email = Column(String)
    date_creation = Column(DateTime)
    telephone = Column(String)
    login = Column(String)
    mdp = Column(String)
    
    __abstract__ = True
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}{tuple(vars(self).values())}'
    
    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
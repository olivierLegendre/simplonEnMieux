from sqlalchemy import Column, String, DateTime, inspect
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from enum import Enum
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
        map_dict = { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
        print(f" map dict {map_dict}")
        map_serialisable = dict()
        for key, value in map_dict.items():
            if isinstance(value, Enum):
                print("la on est chaud !!!")
                map_serialisable[key] = ModeleUtilisateur.get_enum_values(value)
            else:
                map_serialisable[key] = value
        print(f" map serialisable {map_serialisable}")
        return map_serialisable
    
    def get_enum_values(enum):
        print(f" enum class {enum}")
        print(f" to return {enum.name}")
        # return enum.name
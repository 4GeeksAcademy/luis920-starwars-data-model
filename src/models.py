import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
 
class Usuario(Base):
     __tablename__ = 'usuario'
     id = Column(Integer,primary_key=True)
     nombre = Column(String(50), nullable=False)
     apellido = Column(String(70),nullable=False)
     email = Column(String(50),nullable=False) 
     contraseña = Column(String(50),nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer,primary_key=True)
    nombre = Column(String(50),nullable=False)
    altura = Column(Float,nullable=False)
    genero = Column(String(50))
    color_piel = Column(String(50))

class Planeta(Base):
    __tab

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

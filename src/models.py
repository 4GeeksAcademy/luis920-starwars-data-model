import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Float,Date
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
    __tablename__ = 'planeta'
    id = Column(Integer,primary_key=True)
    nombre = Column(String(50),nullable=False)
    diametro = Column(Float,nullable=False)
    clima = Column(String(50),nullable=False)
    terreno = Column(String(50),nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer,primary_key=True)
    usuario_id = Column(Integer,ForeignKey('usuario.id'),nullable =False)
    personaje_id = Column(Integer,ForeignKey('personaje.id'),nullable =False)
    planeta_id = Column(Integer,ForeignKey('planeta.id'),nullable =False)
    fecha_favorito = Column (Date,nullable =False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

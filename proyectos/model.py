from flask_sqlalchemy import Column, Integer, String, ForeignKey
from db import Base


class Proyecto(Base):
    __tablename__ = 'proyectos'
    idProyecto = Column(Integer, primary_key=True, autoincrement=True)
    nombreProyecto = Column(String(50))
    descProyecto = Column(String(150))
    modulos = relationship('modulos', backref='proyectos', lazy=True)


class Modulo(Base):
    __tablename__ = 'modulos'
    idModulo = Column(Integer, primary_key=True, autoincrement=True)
    nombreModulo = Column(String(50))
    descModulo = Column(String(150))
    proyecto_id = Column(Integer, ForeignKey('proyectos.idProyecto'))
    funciones = relationship('Funcion', backref='modulos', lazy=True)

class Funcion(Base):
    __tablename__ = 'funciones'
    idFuncion = Column(Integer, primary_key=True, autoincrement=True)
    nombreFuncion = Column(String(50))
    numCampos = Column(Integer)
    numObjetos = Column(Integer)
    proyecto_id = Column(Integer, ForeignKey('proyectos.idProyecto'))
    modulo_id = Column(Integer, ForeignKey('modulos.idModulo'))
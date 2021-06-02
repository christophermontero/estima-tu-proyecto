from flask_sqlalchemy import Column, Integer, SQLAlchemy, String, ForeignKey
from db import Base
from db import db_session, init_db

db=SQLAlchemy.init_app()


class Proyecto(Base):
    __tablename__ = 'proyectos'
    idProyecto = Column(Integer, primary_key=True, autoincrement=True)
    nombreProyecto = Column(String(50))
    descProyecto = Column(String(150))
    modulos = Base.relationship('modulos', backref='proyectos', lazy=True)

@classmethod
def create(cls, nombre_proyecto, descProyecto):
        proyecto = Proyecto(nombre_proyecto=nombre_proyecto, descProyecto=descProyecto)
        return proyecto.save()

def save(self):
        try:
                db_session.add(self)
                db_session.commit()

                return self
        except:
                return False

class Modulo(Base):
    __tablename__ = 'modulos'
    idModulo = Column(Integer, primary_key=True, autoincrement=True)
    nombreModulo = Column(String(50))
    descModulo = Column(String(150))
    proyecto_id = Column(Integer, ForeignKey('proyectos.idProyecto'))
    funciones = Base.relationship('Funcion', backref='modulos', lazy=True)

class Funcion(Base):
    __tablename__ = 'funciones'
    idFuncion = Column(Integer, primary_key=True, autoincrement=True)
    nombreFuncion = Column(String(50))
    numCampos = Column(Integer)
    numObjetos = Column(Integer)
    proyecto_id = Column(Integer, ForeignKey('proyectos.idProyecto'))
    modulo_id = Column(Integer, ForeignKey('modulos.idModulo'))

    def json(self):
        return {
            'idProyecto': self.id,
            'nombreProyecto': self.username,
            'descProyecto': self.created_at
        }

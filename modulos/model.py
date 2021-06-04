from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from db import db_session, init_db


class Modulo(Base):
    __tablename__ = 'modulos'
    idModulo = Column(Integer, primary_key=True, autoincrement=True)
    nombreModulo = Column(String(50))
    descModulo = Column(String(150))
    proyecto_id = Column(Integer, ForeignKey('proyectos.idProyecto'))
    #funciones = relationship('Funcion', backref='modulos', lazy=True)

    @classmethod
    def create(cls, idModulo, nombreModulo, descModulo, proyecto_id):
        modulo = Modulo(idModulo=idModulo, nombreModulo=nombreModulo, descModulo=descModulo, proyecto_id=proyecto_id)
        return modulo.save()

    def save(self):
        try:
            db_session.add(self)
            db_session.commit()

            return self
        except:
            return False

    def toJson(self):
        return {
            "idModulo": self.idModulo,
            "nombreModulo": self.nombreModulo,
            "descModulo": self.descModulo,
            "proyecto_id": self.proyecto_id,
        }



class Proyecto(Base):
    __tablename__ = 'proyectos'
    idProyecto = Column(Integer, primary_key=True, autoincrement=True)
    nombreProyecto = Column(String(50))
    descProyecto = Column(String(150))
    #modulos = relationship('modulos', backref='proyectos', lazy=True)


class Funcion(Base):
    __tablename__ = 'funciones'
    idFuncion = Column(Integer, primary_key=True, autoincrement=True)
    nombreFuncion = Column(String(50))
    numCampos = Column(Integer)
    numObjetos = Column(Integer)
    proyecto_id = Column(Integer, ForeignKey('proyectos.idProyecto'))
    modulo_id = Column(Integer, ForeignKey('modulos.idModulo'))
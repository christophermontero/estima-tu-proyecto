from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from db import db_session, init_db


class Proyecto(Base):
    __tablename__ = "proyecto"
    idProyecto = Column(Integer, primary_key=True, autoincrement=True)
    nombreProyecto = Column(String(50))
    descProyecto = Column(String(150))
    modulos = relationship("Modulo", back_populates="proyecto", lazy=True)

class Modulo(Base):
    __tablename__ = "modulo"
    idModulo = Column(Integer, primary_key=True, autoincrement=True)
    nombreModulo = Column(String(50))
    descModulo = Column(String(150))
    proyecto_id = Column(Integer, ForeignKey("proyecto.idProyecto"))
    funciones = relationship("Funcion", back_populates="_modulos", lazy=True)
    proyecto = relationship("Proyecto", back_populates="modulos")

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
            db_session.rollback()
            return False

    def toJson(self):
        return {
            "idModulo": self.idModulo,
            "nombreModulo": self.nombreModulo,
            "descModulo": self.descModulo,
            "proyecto_id": self.proyecto_id,
        }

    def delete(self):
        try:
            db_session.delete(self)
            db_session.commit()

            return True
        except:
            db_session.rollback()
            return False

class Funcion(Base):
    __tablename__ = "funcion"
    idFuncion = Column(Integer, primary_key=True, autoincrement=True)
    nombreFuncion = Column(String(50))
    numCampos = Column(Integer)
    numObjetos = Column(Integer)
    complejidad = Column(String(8))
    modulo_id = Column(Integer, ForeignKey("modulo.idModulo"))
    _modulos = relationship("Modulo", back_populates="funciones")
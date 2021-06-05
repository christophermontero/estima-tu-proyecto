from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from db import db_session, init_db


class Proyecto(Base):
    __tablename__ = "proyectos"
    idProyecto = Column(Integer, primary_key=True, autoincrement=True)
    nombreProyecto = Column(String(50))
    descProyecto = Column(String(150))
    # modulos = relationship("modulos", backref="proyectos", lazy=True)

    @classmethod
    def create(cls, idProyecto, nombreProyecto, descProyecto):
        proyecto = Proyecto(idProyecto=idProyecto, nombreProyecto=nombreProyecto, descProyecto=descProyecto)
        return proyecto.save()

    def save(self):
        try:
            db_session.add(self)
            db_session.commit()

            return self
        except:
            db_session.rollback()
            return False

    def delete(self):
        try:
            db_session.delete(self)
            db_session.commit()

            return True
        except:
            return False

    def toJson(self):
        return {
            "idProyecto": self.idProyecto,
            "nombreProyecto": self.nombreProyecto,
            "descProyecto": self.descProyecto,
        }


class Modulo(Base):
    __tablename__ = "modulos"
    idModulo = Column(Integer, primary_key=True, autoincrement=True)
    nombreModulo = Column(String(50))
    descModulo = Column(String(150))
    proyecto_id = Column(Integer, ForeignKey("proyectos.idProyecto"))
    # funciones = relationship("Funcion", backref="modulos", lazy=True)


    def toJson(self):
        return {
           # todo
        }


class Funcion(Base):
    __tablename__ = "funciones"
    idFuncion = Column(Integer, primary_key=True, autoincrement=True)
    nombreFuncion = Column(String(50))
    numCampos = Column(Integer)
    numObjetos = Column(Integer)
    proyecto_id = Column(Integer, ForeignKey("proyectos.idProyecto"))
    modulo_id = Column(Integer, ForeignKey("modulos.idModulo"))

    def toJson(self):
        return {
          # todo
        }

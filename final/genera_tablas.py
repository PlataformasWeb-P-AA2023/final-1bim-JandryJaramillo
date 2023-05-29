from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Establecimiento(Base):
    _tablename_ = 'establecimiento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parroquia_codigo = Column(String(10), ForeignKey('parroquia.codigo'))

    codigo_amie = Column(String(10))
    nombre = Column('nombre', String(250))    
    sostenimiento = Column(String(50))
    tipo_educacion = Column(String(50))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    numero_estudiantes = Column(Integer)
    numero_docentes = Column(Integer)

    parroquia = relationship("Parroquia", back_populates="establecimientos")

class Parroquia(Base):
    _tablename_ = 'parroquia'

    codigo = Column(String(10), primary_key=True)
    nombre = Column(String(250))

    establecimiento_id = Column(Integer, ForeignKey('establecimiento.id'))
    canton_codigo = Column(String(10), ForeignKey('canton.codigo'))

    establecimientos = relationship("Establecimiento", back_populates="parroquia")
    canton = relationship("Canton", back_populates="parroquias")
    

class Canton(Base):
    __tablename__ = 'canton'

    codigo = Column(String(10), primary_key=True)
    nombre = Column(String(250))

    provincia_codigo = Column(String(10), ForeignKey('provincia.codigo'))
    canton_codigo = Column(String(10), ForeignKey('canton.codigo'))

    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")
    
    def __repr__(self):
        return "Jugador: %s - dorsal:%d - posición: %s" % (
                self.nombre, self.dorsal, self.posicion)

class Provincia(Base):
    __tablename__ = 'provincia'

    codigo = Column(String(10), primary_key=True)
    nombre = Column(String(100))

    canton_codigo = Column(String(10), ForeignKey('canton.codigo'))

    cantones = relationship("Canton", back_populates="provincia")
    

    
    def __repr__(self):
        return "Club: nombre=%s deporte=%s fundación=%d" % (
                          self.nombre, 
                          self.deporte, 
                          self.fundacion)
    

Base.metadata.create_all(engine)
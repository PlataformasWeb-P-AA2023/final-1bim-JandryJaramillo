from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=True)

Base = declarative_base()

class Establecimiento(Base):
    __tablename__ = 'establecimiento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parroquia_codigo = Column(String(10), ForeignKey('parroquia.codigo'))
    cod_dis = Column(String(250))

    amie = Column(String(10))
    nombre = Column(String(250))
    sostenimiento = Column(String(50))
    tipo_educacion = Column(String(50))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    num_estudiantes = Column(Integer)
    num_docentes = Column(Integer)

    parroquia = relationship("Parroquia", back_populates="establecimientos")

    def __repr__(self):
        return "Establecimiento: Código Distrito: %s - Código AMIE: %s - Nombre: %s - Sostenimiento: %s - Tipo de Educación: %s - Modalidad: %s - Jornada: %s - Acceso: %s - Número de Estudiantes: %d - Número de Docentes: %d" % (
                self.cod_dis, self.amie, self.nombre, self.sostenimiento,
                self.tipo_educacion, self.modalidad, self.jornada,
                self.acceso, self.num_estudiantes, self.num_docentes)

class Parroquia(Base):
    __tablename__ = 'parroquia'

    codigo = Column(String(10), primary_key=True)
    nombre = Column(String(250))

    canton_codigo = Column(String(10), ForeignKey('canton.codigo'))

    establecimientos = relationship("Establecimiento", back_populates="parroquia")
    canton = relationship("Canton", back_populates="parroquias")

    def __repr__(self):
        return "Parroquia: codigo: %s - nombre: %s" % (
                self.codigo, self.nombre)
    

class Canton(Base):
    __tablename__ = 'canton'

    codigo = Column(String(10), primary_key=True)
    nombre = Column(String(250))

    provincia_codigo = Column(String(10), ForeignKey('provincia.codigo'))
    
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")
    
    def __repr__(self):
        return "Canton: codigo: %s - nombre: %s" % (
                self.codigo, self.nombre)

class Provincia(Base):
    __tablename__ = 'provincia'

    codigo = Column(String(10), primary_key=True)
    nombre = Column(String(100))

    cantones = relationship("Canton", back_populates="provincia")
        
    def __repr__(self):
        return "Provincia: codigo=%s nombre=%s " % (
                          self.codigo, 
                          self.nombre)
    

Base.metadata.create_all(engine)
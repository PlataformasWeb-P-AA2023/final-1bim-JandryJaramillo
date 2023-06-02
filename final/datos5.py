from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_ 

from genera_tablas import Canton, Parroquia, Provincia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

consulta = session.query(Establecimiento).filter(Establecimiento.num_docentes > 100).order_by(Establecimiento.num_estudiantes).all()

print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores:\n")
for e in consulta:
    print(e.nombre, e.num_estudiantes, e.num_docentes)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

consulta2 = session.query(Establecimiento).filter(Establecimiento.num_docentes > 100).order_by(Establecimiento.num_docentes).all()

print("Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores:\n")
for e in consulta2:
    print(e.nombre, e.num_docentes)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

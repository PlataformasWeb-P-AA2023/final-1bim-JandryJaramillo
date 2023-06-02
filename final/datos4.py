from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_ 

from genera_tablas import Canton, Parroquia, Provincia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

consulta = session.query(Establecimiento).join(Establecimiento.parroquia).filter(
    and_(Establecimiento.tipo_educacion.like("%Educación regular%"), Establecimiento.num_docentes >= 40)).order_by(Parroquia.nombre).all()

print("Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena Educación regular en tipo de educación.:\n")
for e in consulta:
    print(e.nombre, e.tipo_educacion, e.num_docentes)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

consulta2 = session.query(Establecimiento).filter(Establecimiento.cod_dis.like("%11D04%")).order_by(Establecimiento.sostenimiento).all()

print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04:\n")
for e in consulta2:
    print(e.sostenimiento, e.nombre, e.cod_dis)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

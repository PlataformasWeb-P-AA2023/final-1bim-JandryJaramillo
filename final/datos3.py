from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_ 

from genera_tablas import Canton, Parroquia, Provincia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

consulta = session.query(Canton).select_from(Canton).join(Canton.parroquias).join(Parroquia.establecimientos).filter(
    or_(Establecimiento.num_docentes.like("%0%"),Establecimiento.num_docentes.like("%5%"),
        Establecimiento.num_docentes.like("%11%"))).distinct()

print("Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores:\n")
for e in consulta:
    print(e.codigo, e.nombre)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

consulta2 = session.query(Establecimiento).join(Establecimiento.parroquia).filter(
    and_(Parroquia.nombre.like("%Pindal%"), Establecimiento.num_estudiantes >= 21)).all()

print("Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21:\n")
for e in consulta2:
    print(e.nombre, e.num_estudiantes)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

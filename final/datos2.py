from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_ 

from genera_tablas import Canton, Parroquia, Provincia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

consulta1 = session.query(Parroquia).select_from(Parroquia).join(Parroquia.establecimientos).filter(Establecimiento.jornada.like("%Matutina y Vespertina%")).distinct()

print("Las parroquias que tienen establecimientos únicamente en la jornada Matutina y Vespertina:\n")
for e in consulta1:
    print(e.codigo, e.nombre)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

consulta2 = session.query(Canton).select_from(Canton).join(Canton.parroquias).join(Parroquia.establecimientos).filter(
    or_(Establecimiento.num_estudiantes.like("%448%"),Establecimiento.num_estudiantes.like("%450%"),
        Establecimiento.num_estudiantes.like("%451%"),Establecimiento.num_estudiantes.like("%454%"),
        Establecimiento.num_estudiantes.like("%458%"),Establecimiento.num_estudiantes.like("%459%"))).distinct()

print("Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459:\n")
for e in consulta2:
    print(e.codigo, e.nombre)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

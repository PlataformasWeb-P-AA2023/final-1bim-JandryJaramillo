from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 

from genera_tablas import Canton, Parroquia, Provincia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

consulta1 = session.query(Establecimiento).join(Parroquia).filter(Parroquia.codigo == 110553).all()

print("Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553:\n")
for e in consulta1:
    print(e.id, e.nombre)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

consulta2 = session.query(Establecimiento).select_from(Establecimiento).join(Parroquia, Establecimiento.parroquia).join(
    Canton, Parroquia.canton).join(Provincia, Canton.provincia).filter(Provincia.nombre.like("%EL ORO%")).all()

print("Todos los establecimientos de la provincia del Oro:\n")
for e in consulta2:
    print(e.id, e.nombre)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

consulta3 = session.query(Establecimiento).select_from(Establecimiento).join(Parroquia, Establecimiento.parroquia).join(
    Canton, Parroquia.canton).filter(Canton.nombre.like("%Portovelo%")).all()

print("Todos los establecimientos del cantón de Portovelo:\n")
for e in consulta3:
    print(e.id, e.nombre)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

consulta4 = session.query(Establecimiento).select_from(Establecimiento).join(Parroquia, Establecimiento.parroquia).join(
    Canton, Parroquia.canton).filter(Canton.nombre.like("%Zamora%")).all()

print("Todos los establecimientos del cantón de Zamora:\n")
for e in consulta4:
    print(e.id, e.nombre)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")
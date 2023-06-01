from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 

from genera_tablas import Canton, Parroquia, Provincia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

consulta1 = session.query(Establecimiento).join(Parroquia).filter(Parroquia.codigo == 110553).all()
#print(consulta1)
print("Consulta1:\n")
for e in consulta1:
    print(e.nombre)

print("----------Fin Consulta ------------")
print("Consulta2:\n")


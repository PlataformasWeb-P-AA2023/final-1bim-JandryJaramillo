from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = open('../data/Listado-Instituciones-Educativas.csv', 'r')

lista = archivo.readlines()

lista = [l.replace(",", "").split("|") for l in lista]

lista2 = (lista[2] , lista[3] )

print(lista2)




archivo.close()
#session.commit()
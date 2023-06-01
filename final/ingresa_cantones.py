from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
# necesitamos 2 librerias para manejar más fácil el csv
# pip install numpy para instalar NumPy
# pip install pandas para instalar Pandas.

from genera_tablas import Provincia, Canton

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = pd.read_csv('../data/Listado-Instituciones-Educativas.csv', delimiter='|')

cantones = archivo[['Provincia', 'Código División Política Administrativa  Cantón', 'Cantón']]

print(cantones)

noRepetir = cantones.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val1 = row['Provincia']
    val2 = row['Código División Política Administrativa  Cantón']
    val3 = row['Cantón']

    provincia = session.query(Provincia).filter_by(nombre=val1).one()

    print(provincia)

    canton = Canton(codigo=val2, nombre=val3, provincia=provincia)
    print(canton)
    session.add(canton)

session.commit()
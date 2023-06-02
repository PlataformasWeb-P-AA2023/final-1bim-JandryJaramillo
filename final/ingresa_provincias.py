from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
# necesitamos 2 librerias para manejar más fácil el csv
# pip install numpy para instalar NumPy
# pip install pandas para instalar Pandas.

from genera_tablas import Provincia

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

archivo = pd.read_csv('../data/Listado-Instituciones-Educativas.csv', delimiter='|')

provincias = archivo[['Código División Política Administrativa Provincia', 'Provincia']]

print(provincias)

noRepetir = provincias.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val1 = row['Código División Política Administrativa Provincia']
    val2 = row['Provincia']
    provincia = Provincia(codigo=val1, nombre=val2)
    print(provincia)
    session.add(provincia)

session.commit()
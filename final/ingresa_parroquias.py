from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
# necesitamos 2 librerias para manejar más fácil el csv
# pip install numpy para instalar NumPy
# pip install pandas para instalar Pandas.

from genera_tablas import Canton, Parroquia

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

archivo = pd.read_csv('../data/Listado-Instituciones-Educativas.csv', delimiter='|')

parroquias = archivo[['Cantón', 'Código División Política Administrativa  Parroquia', 'Parroquia']]

print(parroquias)

noRepetir = parroquias.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val1 = row['Cantón']
    val2 = row['Código División Política Administrativa  Parroquia']
    val3 = row['Parroquia']

    canton = session.query(Canton).filter_by(nombre=val1).one()

    print(canton)

    parroquia = Parroquia(codigo=val2, nombre=val3, canton=canton)
    print(parroquia)
    session.add(parroquia)

session.commit()
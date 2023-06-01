from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
# necesitamos 2 librerias para manejar más fácil el csv
# pip install numpy para instalar NumPy
# pip install pandas para instalar Pandas.

from genera_tablas import Canton, Parroquia, Provincia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = pd.read_csv('../data/Listado-Instituciones-Educativas.csv', delimiter='|')

establecimientos = archivo[['Código División Política Administrativa  Parroquia',\
                            'Código de Distrito', 'Nombre de la Institución Educativa',\
                            'Código AMIE', 'Sostenimiento', 'Tipo de Educación',\
                            'Modalidad', 'Jornada','Acceso (terrestre/ aéreo/fluvial)',\
                            'Número de estudiantes', 'Número de docentes']]

print(establecimientos)

noRepetir = establecimientos.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val1 = row['Código División Política Administrativa  Parroquia']
    val2 = row['Código de Distrito']
    val3 = row['Nombre de la Institución Educativa']
    val4 = row['Código AMIE']
    val5 = row['Sostenimiento']
    val6 = row['Tipo de Educación']
    val7 = row['Modalidad']
    val8 = row['Jornada']
    val9 = row['Acceso (terrestre/ aéreo/fluvial)']
    val10 = row['Número de estudiantes']
    val11 = row['Número de docentes']

    parroquia = session.query(Parroquia).filter_by(codigo=val1).one()

    print(parroquia)

    establecimiento = Establecimiento(parroquia_codigo=val1, cod_dis=val2, amie=val4,
                                      nombre=val3, sostenimiento=val5, tipo_educacion=val6,
                                      modalidad=val7, jornada=val8, acceso=val9,
                                      num_estudiantes=val10, num_docentes=val11,
                                      parroquia=parroquia)

    print(establecimiento)
    session.add(establecimiento)

session.commit()
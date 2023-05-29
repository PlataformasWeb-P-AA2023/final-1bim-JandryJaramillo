from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Establecimiento, Parroquia, Canton, Provincia

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = open('data/Listado-Instituciones-Educativas.csv', 'r')

lista = archivo.readlines()

lista = [l.replace(",", "").split("|") for l in lista]

for l in lista:        
        club = Club(nombre= l[0] , deporte= l[1] , fundacion= int(l[2][0:4]))
        
        session.add(club)


archivo2 = open('data/datos_jugadores.txt', 'r')

lista2 = archivo2.readlines()

lista2 = [l2.replace("\n", "").split(";") for l2 in lista2]

for l2 in lista2:        
        club = session.query(Club).filter_by(nombre=l2[0]).one()
        jugadores = Jugador(nombre= l2[3], dorsal= int(l2[2]), posicion= l2[1], club= club)
        
        session.add(jugadores)

archivo.close()
archivo2.close()
session.commit()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 

from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

clubs = session.query(Club).all()

print("Presentación de Clubs")
for s in clubs:
    print("%s" % (s))
    print("---------")

jugadores = session.query(Jugador).all()

print("Jugadores")
for s in jugadores:
    print("%s" % (s))
    print("---------")
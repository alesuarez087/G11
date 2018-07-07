from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

Base = declarative_base()


class Socio(Base):
	__tablename__ = 'Socio'
	id_socio = Column(Integer, primary_key=True)
	dni = Column(Integer, unique=True)
	nombre = Column(String(250))
	apellido = Column(String(250))

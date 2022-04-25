from sqlalchemy import Column, Integer, String 
from config import Base

class Persona(Base):
    __tablename__ = 'persona'

    id=Column(Integer, primary_key=True)
    nombre=Column(String)
    edad=Column(Integer)



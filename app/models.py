from sqlalchemy import Column, Integer, String, ForeignKey
from config import Base

class Persona(Base):
    __tablename__ = 'persona'

    id=Column(Integer, primary_key=True)
    nombre=Column(String)
    edad=Column(Integer)


class Trabajo(Base):
    __tablename__ = 'trabajo'

    id=Column(Integer, primary_key=True)
    nombre=Column(String)
    persona_id = Column(Integer, ForeignKey('persona.id'))


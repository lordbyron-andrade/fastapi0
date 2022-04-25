from sqlalchemy.orm import Session 
from models import Persona 
from schemas import PersonaSchema 

def get_personas(db:session, skip:int=0,limit:int=100):
    return db.query(Persona).offset(skip).limit(limit).all()

def get_persona_by_id(db:Session, p_id:int):
    return db.query(Persona).filter(Persona.id == p_id).fisrst()

def crear_persona(db:Session, persona: PersonaSchema):
    _persona = Persona(nombre = persona.nombre)
    db.add(_persona)
    db.commit()
    db.refresh(_persona)
    return _persona 

def eliminar_persona(db:Session, p_id:int):
    _persona = get_persona_by_id(p_id)
    db.delete(_persona)
    db.commit()

def actualizar_persona(db:Session, p_id:int, nombre:str):
    _p = get_persona_by_id(p_id)
    _p.nombre = nombre
    db.commit();
    db.refresh(_p)
    return _p
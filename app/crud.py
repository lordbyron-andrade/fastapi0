from sqlalchemy.orm import Session 
from models import Persona, Trabajo 
from schemas import PersonaSchema, TrabajoSchema


def get_personas(db:Session, skip:int=0,limit:int=100):
    return db.query(Persona).offset(skip).limit(limit).all()

def get_trabajos(db:Session, skip:int=0,limit:int=100):
    return db.query(Trabajo).offset(skip).limit(limit).all()

def get_persona_by_id(db:Session, p_id:int):
    return db.query(Persona).filter(Persona.id == p_id).first()

def get_trabajo_by_id(db:Session, tr_id:int):
    return db.query(Trabajo).filter(Trabajo.id == tr_id).first()

def crear_persona(db:Session, persona: PersonaSchema):
    _persona = Persona(nombre = persona.nombre, edad=persona.edad)
    db.add(_persona)
    db.commit()
    db.refresh(_persona)
    return _persona 

def crear_trabajo(db:Session, trabajo: TrabajoSchema):
    _tr = Trabajo(nombre = trabajo.nombre, persona_id = trabajo.persona_id)
    db.add(_tr)
    db.commit()
    db.refresh(_tr)
    return _tr

def eliminar_persona(db:Session, p_id:int):
    _persona = get_persona_by_id(db, p_id)
    db.delete(_persona)
    db.commit()

def eliminar_trabajo(db:Session, t_id:int):
    _tr = get_persona_by_id(db, t_id)
    db.delete(_tr)
    db.commit()

def actualizar_persona(db:Session, p_id:int, nombre:str, edad:int):
    _p = get_persona_by_id(db, p_id)
    _p.nombre = nombre
    _p.edad = edad
    db.commit();
    db.refresh(_p)
    return _p

def actualizar_trabajo(db:Session, tr_id:int, nombre:str, persona_id:int):
    _tr = get_persona_by_id(db, tr_id)
    _tr.nombre = nombre
    _tr.persona_id = persona_id
    db.commit();
    db.refresh(_tr)
    return _tr
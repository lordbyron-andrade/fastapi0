from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal 
from sqlalchemy.orm import Session 
from schemas import PersonaSchema, RequestPersona, Response 
import crud 

router = APIRouter() 

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close() 

@router.post('/create')
async def create(request:RequestPersona,db:Session=Depends(get_db)):
    crud.crear_persona(db, request.parameter)
    return Response(code=200,status="Ok",message="Se creo la persona con exito").dict(exclude_none=True)

@router.get("/")
async def get(db: Session = Depends(get_db)):
    _p = crud.get_personas(db,0,100)
    return Response(code=200,status="Ok",message="Se leyeron todos los datos con exito").dict(exclude_none=True)


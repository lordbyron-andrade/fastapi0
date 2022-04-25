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
    return Response(code=200,status="Ok",message="Se leyeron todos los datos con exito",result=_p).dict(exclude_none=True)

@router.patch("/update")
async def actualizar_persona(request: RequestPersona, db: Session = Depends(get_db)):
    _p = crud.actualizar_persona(db, p_id=request.parameter.id,
                                    nombre=request.parameter.nombre, edad=request.parameter.edad)
    return Response(status="Ok", code="200", message="Success update data", result= _p)

@router.delete("/delete")
async def eliminar_persona(request: RequestPersona,  db: Session = Depends(get_db)):
    crud.eliminar_persona(db, p_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

@router.delete("/delete2/{id}")
async def eliminar_persona2(id:int,  db: Session = Depends(get_db)):
    crud.eliminar_persona(db, p_id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
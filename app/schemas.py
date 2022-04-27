from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field 
from pydantic.generics import GenericModel 

T = TypeVar('T')

class PersonaSchema(BaseModel):
    id: Optional[int]=None
    nombre: Optional[str]=None
    edad: Optional[int]=None

    class Config: 
        orm_mode = True 
        
class TrabajoSchema(BaseModel):
    id: Optional[int]=None
    nombre: Optional[str]=None
    persona_id: Optional[int]=None

    class Config: 
        orm_mode = True 

class RequestTrabajo(BaseModel): 
    parameter: TrabajoSchema = Field(...) 

class RequestPersona(BaseModel): 
    parameter: PersonaSchema = Field(...) 

class Response (GenericModel,Generic[T]):
    code: str 
    status: str 
    message: str
    result: Optional[T] 


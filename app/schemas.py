from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field 
from pydantic.generics import GenericModel 

T = TypeVar('T')

class PersonaSchema(BaseModel):
    id: Optional[int]=None
    nombre: Optional[str]=None

    class Config: 
        orm_mode = True 

class RequestPersona(BaseModel): 
    parameter: PersonaSchema = Field(...) 

class Response (GenericModel,Generic[T]):
    code: str 
    status: str 
    message: str
    result: Optional[T] 


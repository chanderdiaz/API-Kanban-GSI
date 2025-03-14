from pydantic import BaseModel
from typing import Optional

class TableroModel(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str]

    class Config:
        orm_mode = True

class ListaModel(BaseModel):
    id: int
    id_tablero: int
    nombre: str

    class Config:
        orm_mode = True

class TareaModel(BaseModel):
    id: int
    id_lista: int
    titulo: str
    descripcion: str = ""

    class Config:
        orm_mode = True
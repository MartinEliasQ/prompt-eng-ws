from pydantic import BaseModel
from typing import Literal

class OrdernItems(BaseModel):
    cantidad: int
    producto: str
    descripcion: str


class Orden(BaseModel):
    ref: str
    org: str
    dest: str
    notas: str
    items: list[OrdernItems]
    type: Literal["orden", "spam"]


class OrdenResponse(BaseModel):
    
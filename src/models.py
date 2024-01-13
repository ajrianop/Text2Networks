from pydantic import BaseModel
from typing import List, Optional


class Pagina(BaseModel):
    n_pagina: int
    contenido: str


class Libro(BaseModel):
    nombre: str
    numero_paginas: int
    contenido: Optional[List[Pagina]]

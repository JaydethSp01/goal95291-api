from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Categoria(BaseModel):
    id: int
    nombre: str

categorias_db = [
    Categoria(id=1, nombre="Ropa"),
    Categoria(id=2, nombre="Accesorios")
]

@router.get("/categoria", response_model=List[Categoria])
async def get_categorias():
    return categorias_db

@router.post("/categoria", response_model=Categoria)
async def create_categoria(categoria: Categoria):
    categorias_db.append(categoria)
    return categoria

@router.put("/categoria/{categoria_id}", response_model=Categoria)
async def update_categoria(categoria_id: int, categoria: Categoria):
    for index, c in enumerate(categorias_db):
        if c.id == categoria_id:
            categorias_db[index] = categoria
            return categoria
    raise HTTPException(status_code=404, detail="Categoria not found")

@router.delete("/categoria/{categoria_id}")
async def delete_categoria(categoria_id: int):
    for index, c in enumerate(categorias_db):
        if c.id == categoria_id:
            del categorias_db[index]
            return {"message": "Categoria deleted"}
    raise HTTPException(status_code=404, detail="Categoria not found")

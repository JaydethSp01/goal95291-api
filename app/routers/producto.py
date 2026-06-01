from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria_id: int

productos_db = [
    Producto(id=1, nombre="Camiseta", precio=19.99, categoria_id=1),
    Producto(id=2, nombre="Pantalón", precio=39.99, categoria_id=2)
]

@router.get("/producto", response_model=List[Producto])
async def get_productos():
    return productos_db

@router.post("/producto", response_model=Producto)
async def create_producto(producto: Producto):
    productos_db.append(producto)
    return producto

@router.put("/producto/{producto_id}", response_model=Producto)
async def update_producto(producto_id: int, producto: Producto):
    for index, p in enumerate(productos_db):
        if p.id == producto_id:
            productos_db[index] = producto
            return producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.delete("/producto/{producto_id}")
async def delete_producto(producto_id: int):
    for index, p in enumerate(productos_db):
        if p.id == producto_id:
            del productos_db[index]
            return {"message": "Producto deleted"}
    raise HTTPException(status_code=404, detail="Producto not found")

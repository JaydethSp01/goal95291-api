from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Alerta(BaseModel):
    id: int
    producto_id: int
    mensaje: str

alertas_db = [
    Alerta(id=1, producto_id=1, mensaje="Stock bajo para camiseta"),
    Alerta(id=2, producto_id=2, mensaje="Stock bajo para pantalón")
]

@router.get("/alerta", response_model=List[Alerta])
async def get_alertas():
    return alertas_db

@router.post("/alerta", response_model=Alerta)
async def create_alerta(alerta: Alerta):
    alertas_db.append(alerta)
    return alerta

@router.delete("/alerta/{alerta_id}")
async def delete_alerta(alerta_id: int):
    for index, a in enumerate(alertas_db):
        if a.id == alerta_id:
            del alertas_db[index]
            return {"message": "Alerta deleted"}
    raise HTTPException(status_code=404, detail="Alerta not found")

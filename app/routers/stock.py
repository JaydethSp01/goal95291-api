from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Stock(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    talla: str

stocks_db = [
    Stock(id=1, producto_id=1, cantidad=50, talla="M"),
    Stock(id=2, producto_id=2, cantidad=30, talla="L")
]

@router.get("/stock", response_model=List[Stock])
async def get_stocks():
    return stocks_db

@router.post("/stock", response_model=Stock)
async def create_stock(stock: Stock):
    stocks_db.append(stock)
    return stock

@router.put("/stock/{stock_id}", response_model=Stock)
async def update_stock(stock_id: int, stock: Stock):
    for index, s in enumerate(stocks_db):
        if s.id == stock_id:
            stocks_db[index] = stock
            return stock
    raise HTTPException(status_code=404, detail="Stock not found")

@router.delete("/stock/{stock_id}")
async def delete_stock(stock_id: int):
    for index, s in enumerate(stocks_db):
        if s.id == stock_id:
            del stocks_db[index]
            return {"message": "Stock deleted"}
    raise HTTPException(status_code=404, detail="Stock not found")

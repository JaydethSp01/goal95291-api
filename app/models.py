from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int
    name: str
    price: float
    category_id: int

class Category(BaseModel):
    id: int
    name: str

class Supplier(BaseModel):
    id: int
    name: str
    contact_info: str

class Stock(BaseModel):
    id: int
    product_id: int
    size: str
    quantity: int

class Alert(BaseModel):
    id: int
    product_id: int
    message: str

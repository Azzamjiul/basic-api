from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str
    category: Optional[str] = None
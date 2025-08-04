from typing import Optional
from pydantic import BaseModel, Field

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

class NoteItem(BaseModel):
    id: int
    title: str
    content: str

class NoteResponse(BaseModel):
    message: str
    items: list[NoteItem]

class NoteItemResponse(BaseModel):
    message: str
    item: NoteItem

class NoteAdd(BaseModel):
    title: str = Field(..., min_length=10, max_length=100)
    content: Optional[str] = Field(None, min_length=0, max_length=1000)

class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=10, max_length=100)
    content: Optional[str] = Field(None, min_length=0, max_length=1000)
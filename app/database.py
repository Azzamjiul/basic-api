from typing import Optional
from sqlmodel import SQLModel, Field

class Note(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(default="Untitled Note")
    content: Optional[str] = Field(default=None, nullable=True)
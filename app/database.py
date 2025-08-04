import os
from typing import Optional
from dotenv import load_dotenv
from sqlmodel import SQLModel, Field, create_engine, Session

load_dotenv(override=True)

engine = create_engine(os.environ.get("DATABASE_URL", ""), echo=True)

def get_db_session():
    with Session(engine) as session:
        yield session

class Note(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(default="Untitled Note")
    content: Optional[str] = Field(default=None, nullable=True)
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlmodel import Session, select
from app.database import Note, get_db_session
from app.schema import (
    NoteItem,
    NoteResponse,
    NoteItemResponse,
    NoteAdd,
    NoteUpdate,
)


notes_router = APIRouter(prefix="/notes", tags=["Notes"])


@notes_router.get("/")
def list_notes(db: Session = Depends(get_db_session)):
    notes = db.exec(select(Note)).all()
    return notes


@notes_router.post("/", response_model=NoteItemResponse)
def create_note(note: NoteAdd, db: Session = Depends(get_db_session)):
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return NoteItemResponse(message="Note created successfully", item=NoteItem(
        id=new_note.id,
        title=new_note.title,
        content=new_note.content
    ))
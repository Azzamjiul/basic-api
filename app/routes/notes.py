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
from starlette import status

notes_router = APIRouter(prefix="/notes", tags=["Notes"])


@notes_router.get("/", status_code=status.HTTP_200_OK)
def list_notes(db: Session = Depends(get_db_session)):
    notes = db.exec(select(Note)).all()
    return notes


@notes_router.post("/", response_model=NoteItemResponse, status_code=status.HTTP_200_OK)
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


@notes_router.get("/{note_id}", response_model=NoteItemResponse, status_code=status.HTTP_200_OK)
def get_note(note_id: int, db: Session = Depends(get_db_session)):
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteItemResponse(message="Note retrieved successfully", item=NoteItem(
        id=note.id,
        title=note.title,
        content=note.content
    ))


@notes_router.put("/{note_id}", response_model=NoteItemResponse, status_code=status.HTTP_200_OK)
def update_note(note_id: int, note_update: NoteUpdate, db: Session = Depends(get_db_session)):
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note.title = note_update.title
    note.content = note_update.content
    db.add(note)
    db.commit()
    db.refresh(note)
    return NoteItemResponse(message="Note updated successfully", item=NoteItem(
        id=note.id,
        title=note.title,
        content=note.content
    ))


@notes_router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db_session)):
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()
    return None
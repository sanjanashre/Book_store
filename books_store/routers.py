from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from books_store.database import SessionLocal
from books_store import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/books", response_model=list[schemas.BookResponse])
def read_books(db: session = Depends(get_db)):
    return crud.get_books(db)

@router.post("/books", response_model=schemas.BookResponse)
def create_new_book(book: schemas.BookCreate, db: session = Depends(get_db)):
    return crud.create_book(db, book)





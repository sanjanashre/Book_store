from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from books_store.database import get_db
from books_store import crud, schemas


router = APIRouter()



@router.get("/books", response_model=list[schemas.BookResponse])
def read_books(db: session = Depends(get_db)):
    books= crud.get_books(db)
    return [schemas.BookResponse.from_orm(book) for book in books]

@router.post("/books", response_model=schemas.BookResponse)
def create_new_book(book: schemas.BookCreate, db: session = Depends(get_db)):
    return crud.create_book(db,book)

@router.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: str, db: session = Depends(get_db)):
    return crud.get_book(db, book_id)

@router.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: str, book: schemas.BookCreate, db: session = Depends(get_db)):
    return crud.update_book(db, book_id, book)

@router.delete("/books/{book_id}", response_model=schemas.BookResponse)
def delete_book(book_id: str, db: session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if book:
        crud.delete_book(db, book_id)
        return book
    return None 
from sqlalchemy.orm import Session
from books_store.models import Book
from books_store.schemas import BookResponse
from sqlalchemy.dialects.postgresql import UUID

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: str):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: BookResponse):
    db_book = Book (
        id=str(book.id),title=book.title, author=book.author,
        published_year=book.published_year,
        isbn=book.isbn,price=book.price,created_at=book.created_at )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

from sqlalchemy.orm import Session
from books_store.models import Book
from books_store.schemas import BookResponse,BookCreate
from sqlalchemy.dialects.postgresql import UUID

def get_books(db: Session):
    return db.query(Book).all()
    
def get_book(db: Session, book_id: str):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: str, book: BookCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book: 
        db_book.title = book.title
        db_book.author = book.author
        db_book.published_year = book.published_year
        db_book.isbn = book.isbn
        db_book.price = book.price
        
        db.commit()
        db.refresh(db_book)
    return db_book

"""def create_book(db: Session, book: BookCreate):
    db_book = Book (
        title=book.title, author=book.author,
        published_year=book.published_year,
        isbn=book.isbn,price=book.price )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: str, book: BookCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    db_book= Book ( title = book.title,author = book.author,published_year = book.published_year,
                   isbn = book.isbn,price = book.price)
    db.commit()
    db.refresh(db_book)
    return db_book"""

def delete_book(db: Session, book_id: str):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
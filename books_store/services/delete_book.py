from fastapi import HTTPException, status
from database import session
from books_store.schemas import RetrieveBooksSchema
from books_store.models import Book



"""def delete_book(db: Session, book_id: str):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()"""

class DeleteBook:

    def __init__ (self,payload:RetrieveBooksSchema,session:session,book_id:int):
        self.payload=payload
        self.session=session
        self.book_id=book_id

    def get_book(self):
        return self.session.query(Book).filter(Book.id == self.book_id).first()
    
    def delete_book(self,book:Book):
    
        self.session.delete(book)
        self.session.commit()
    
    
    def run(self):
        book = self.get_book()
        self.delete_book(book)
        
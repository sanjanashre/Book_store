from fastapi import HTTPException, status
from sqlalchemy.orm import session
from books_store.schemas import AddBookRequestSchema
from books_store.models import Book
from sqlalchemy import cast
from uuid import UUID

class UpdateBookService:
    """Service class to Update a book in database """
    def __init__(self, session:session, payload:AddBookRequestSchema, book_id:int):
        self.session = session
        self.payload = payload
        self.book_id = book_id


    def get_book_from_id(self) -> Book:
        """
        Query book from database. If not found return exception
        """
        return self.session.query(Book).filter(Book.id== self.book_id).first()

    def update_book(self, book:Book):
        """
        Only update the details of the book
        """
        if book:
            book.title=self.payload.title
            book.author=self.payload.author
            book.published_year=self.payload.published_year
            book.isbn=self.payload.isbn
            book.price=self.payload.price

        return {"detail","book not found"}

    def run(self):
        """
        Use this as a runner function
        """
        book=self.get_book_from_id()
        self.update_book(book)
        return book
       
        
    
            
   
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from books_store.schemas import RetrieveBooksSchema
from books_store.models import Book
from uuid import UUID
from sqlalchemy import cast


class RetrieveBookDetails:
    """Service class to retrieve book details from the database."""
    def __init__(self,session:Session,book_id:UUID):
        """
        Constructor for RetrieveBookDetails 
        """
        self.session=session
        self.book_id=book_id
    
    def retrieve_book(self)-> Book:
         
        """Retrieves a book by its ID.
           Returns:
            Book: The retrieved book instance if found."""
        return self.session.query(Book).filter(Book.id == self.book_id).first()

    def run(self):
        """Runner function to execute the retrieval operation."""
        return self.retrieve_book()
    
class RetrieveAllBooks:
    
    def __init__(self, session: Session):
        """Constructor for RetrieveAllBooks"""
        self.session = session

    def retrieve_all(self)-> Book:
          """Retrieves all the list of all books """
          return self.session.query(Book).all()


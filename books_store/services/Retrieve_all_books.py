from fastapi import HTTPException, status
from database import session
from books_store.schemas import RetrieveBooksSchema
from books_store.models import Book


class RetrieveAllBooks:
    """Service class to retrieve all books from the database."""
    def __init__(self,session:session,payload:RetrieveBooksSchema):
        """
        Constructor for RetrieveBookDetails 
        """
        self.session=session
        self.payload=payload
    
    def Retrieve_all(self)-> Book:
          return self.session.query(Book).all()

    def run(self):
        """Runner function to execute the retrieval operation."""
        self.Retrieve_all()
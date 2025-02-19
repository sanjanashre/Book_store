from fastapi import HTTPException, status
from database import session
from books_store.schemas import RetrieveBooksSchema
from books_store.models import Book


class RetrieveBookDetails:
    """Service class to retrieve book details from the database."""
    def __init__(self,session:session,payload:RetrieveBooksSchema,book_id:int):
        """
        Constructor for RetrieveBookDetails 
        """
        self.session=session
        self.payload=payload
        self.book_id=book_id
    
    def Retrieve_book(self)-> Book:
         
        """Retrieves a book by its ID.
           Returns:
            Book: The retrieved book instance if found."""
        return self.session.query(Book).filter(Book.id == self.book_id).first()

    def run(self):
        """Runner function to execute the retrieval operation."""
        self.Retrieve_book()




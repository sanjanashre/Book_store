from fastapi import HTTPException, status
from database import session
from books_store.schemas import RetrieveBooksSchema
from books_store.models import Book


class DeleteBook:
    """Constructor for delete a book
    """
    def __init__ (self,payload:RetrieveBooksSchema,session:session,book_id:int):
        self.payload=payload
        self.session=session
        self.book_id=book_id

    def get_book(self):
        """delete a book by its id

        Returns:
            Book:Delete a book if found
        """
        return self.session.query(Book).filter(Book.id == self.book_id).first()
    
    def delete_book(self,book:Book):
        
        self.session.delete(book)
        self.session.commit()
    
    
    def run(self):
        """Runner function to execute the retrieval operation."""
        book = self.get_book()
        self.delete_book(book)
        
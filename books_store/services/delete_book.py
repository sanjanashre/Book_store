from fastapi import HTTPException, status
from sqlalchemy.orm import session
from books_store.schemas import RetrieveBooksSchema
from books_store.models import Book
from uuid import UUID
from sqlalchemy import cast


class DeleteBook:
    """Constructor for delete a book
    """
    def __init__ (self,session:session,book_id:str):
        self.session=session
        self.book_id=book_id

    def get_book(self):
        """delete a book by its id

        Returns:
            Book:Delete a book if found
        """
        book=self.session.query(Book).filter(Book.id== self.book_id).first()
        return book
    
    def delete_book(self,book:Book):
        
        self.session.delete(book)
        self.session.commit()
    
    
    def run(self):
        """Runner function to execute the retrieval operation."""
        book = self.get_book()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        self.delete_book(book)
from fastapi import HTTPException, status

from books_store.models import Book


class UpdateBookService:

    def __init__(self, session, payload, book_id):
        self.session = session
        self.payload = payload
        self.book_id = book_id

    def get_book_from_id(self) -> Book:
       """
       Query book from database. If not found return exception
       """

    def update_book(self, book):
        """
        Only update the details of the book
        """

    def run(self):
       """
       Use this as a runner function
       """

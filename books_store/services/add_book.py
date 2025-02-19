from sqlalchemy.orm import Session

from books_store.models import Book
from books_store.schemas import AddBookRequestSchema


class AddBookService:
    """
    Service class to add a book in the database.
    """

    def __init__(self, session: Session,
                 payload: AddBookRequestSchema) -> None:
        """
        Constructor for AddBookService
        """
        self.session = session
        self.payload = payload

    def add_book(self) -> None:
        """
        Adds a new book to the session.
        """
        book = Book(
            title=self.payload.title,
            author=self.payload.author,
            published_year=self.payload.published_year,
            isbn=self.payload.isbn,
            price=self.payload.price,
        )
        self.session.add(book)
        self.session.refresh()

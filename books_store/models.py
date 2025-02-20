from sqlalchemy import Column, String, Integer, Float
from books_store.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime
from datetime import datetime
import uuid


class Book(Base):
    __tablename__ = "books"

    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)
    isbn = Column(String(13), nullable=True, unique=True)
    price = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    library_id = Column(String(255), nullable=True)


# TODO:
# Add a new model called Library
# Add fields such as id, name, address_line_one, address_line_two, city, state, country, zip_code
# GET /libraries - This endpoint will give me a list of all the libraries
# POST /libraries - This endpoint allow you to add a library
## Schema - LibraryRequestSchema
## name, address_line_one, address_line_two, city, state, country, zip_code

# TODO:
# Add a new model called LibraryBooks
# Add fields like library_id, book_id
# Add API endpoints to add books to a library
# GET /libraries/{library_id}/books - This endpoint will give me a list of all the books in a library
# POST /libraries/{library_id}/books - This endpoint allow you to add a book to a library
## Schema - LibraryBookRequestSchema
# class LibraryBookRequestSchema(BaseModel):
#   book_ids: list[uuid]

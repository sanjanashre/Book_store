# from dbm.ndbm import library
from sqlalchemy import Column, String, Integer, Float
from books_store.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
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
    
    #relationships for library & librarybooks

    libraryBooks = relationship("LibararyBooks",back_populates="book")
    libraries = relationship("Library",back_populates="books") 


class Library(Base):
    __tablename__ = "libraries"

    id = Column(String(225),primary_key=True,default=uuid.uuid4)
    name = Column(String,nullable=False)
    address_line_one = Column(String,nullable=False) 
    address_line_two = Column(String,nullable=False)
    city = Column(String,nullable=False)
    state = Column(String,nullable=False)
    country = Column(String,nullable=False)
    zip_code = Column(Integer,nullable=False)

    #relationships for books & librarybooks

    books = relationship("Book",back_populates="libraries")
    librarybooks = relationship("LibraryBooks",back_populates="library")

class LibraryBooks(Base):
    __tablename__ = "librarybooks"

    id = Column(String(225),primary_key=True,default=uuid.uuid4)
    book_id =  Column(String(225),ForeignKey("books.id"))
    library_id = Column(String(225),ForeignKey("libraries.id"))

    # relationship for books and library table 

    book = relationship("Book",back_populates="librarybooks")
    library = relationship("Library",back_populates="librarybooks")
    



# TODO:
# Add a new model called Library *
# Add fields such as id, name, address_line_one, address_line_two, city, state, country, zip_code *
# GET /libraries - This endpoint will give me a list of all the libraries
# POST /libraries - This endpoint allow you to add a library
## Schema - LibraryRequestSchema
## name, address_line_one, address_line_two, city, state, country, zip_code

# TODO:
# Add a new model called LibraryBooks *
# Add fields like library_id, book_id *
# Add API endpoints to add books to a library
# GET /libraries/{library_id}/books - This endpoint will give me a list of all the books in a library
# POST /libraries/{library_id}/books - This endpoint allow you to add a book to a library
## Schema - LibraryBookRequestSchema
# class LibraryBookRequestSchema(BaseModel):
#   book_ids: list[uuid]

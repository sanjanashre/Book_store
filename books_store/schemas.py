from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, UUID4


class BaseDetailSchema(BaseModel):
    detail: str


class BaseBookSchema(BaseModel):
    title: str
    author: str
    published_year: int
    isbn: str
    price: int


class AddBookRequestSchema(BaseBookSchema):
    pass


class RetrieveBooksSchema(BaseBookSchema):
    id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True

    @classmethod
    def from_orm(cls, obj):
        """Manually convert UUID to a string."""
        return cls(
            id=str(obj.id),
            title=obj.title,
            author=obj.author,
            published_year=obj.published_year,
            isbn=obj.isbn,
            price=obj.price,
            created_at=obj.created_at,
        )


class LibraryRequestSchema(BaseModel):
    """schemas for library 
    """
    name: str
    address_line_one: str
    address_line_two: str
    city: str
    state: str
    country: str
    zip_code: int


class RetrieveLibrarySchema(LibraryRequestSchema):
    """Schemas for retrieve a Library"""
    id: UUID

   
 


class LibraryBookRequestSchema(BaseModel):
    
    id: UUID


class AddLibraryBookSchema(BaseModel):
    """Schema for adding books into a library"""

    book_ids: list[UUID]


class RetrieveLibraryBookSchema(BaseModel):
    """retrieve books from schema"""
    id: UUID
    book: RetrieveBooksSchema

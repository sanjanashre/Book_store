from pydantic import BaseModel,UUID4
from typing import Optional
from datetime import datetime
from uuid import UUID

class BookBase(BaseModel):
    title: str
    author: str
    published_year: int
    isbn: str
    price: int
   
class BookCreate(BookBase):
    pass
class BookResponse(BookBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attribute = True
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
            created_at=obj.created_at
        )

       
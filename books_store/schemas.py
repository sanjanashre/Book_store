from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlalchemy import UUID

class BookBase(BaseModel):
    id:str
    title: str
    author: str
    published_year: int
    isbn: str
    price: int
    created_at: datetime

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: str



    class Config:
        orm_mode = True


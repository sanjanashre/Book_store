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
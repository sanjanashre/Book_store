from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 

DATABASE_URL = "postgresql+psycopg2://postgres:sanjana@localhost:5432/book_store"

engine= create_engine(DATABASE_URL)

sessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


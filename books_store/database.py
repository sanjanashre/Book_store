from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 

#postgresql+psycopg2://postgres:postgres@tawazun-db:5432/tawazun
DATABASE_URL = "postgresql+psycopg2://postgres:sanjana@localhost:5432/book_store"

engine= create_engine(DATABASE_URL)

SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()





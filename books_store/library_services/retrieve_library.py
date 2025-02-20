from sqlalchemy.orm import Session

from books_store.models import Library
from books_store.schemas import RetrieveLibrarySchema

class RetrieveLibraryDetails:

    def __init__(self,session:Session,payload:RetrieveLibrarySchema,library_id:str) ->None:
        self.session=session
        self.payload=payload
        self.library_id =library_id

    def get_library(self,book_id):
        return self.session.query(Library).filter(Library.id == self.library_id).first()
    
    def run(self):
        self.get_library()





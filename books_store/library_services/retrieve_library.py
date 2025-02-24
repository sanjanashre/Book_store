from sqlalchemy.orm import Session

from books_store.models import Library
from books_store.schemas import RetrieveLibrarySchema

class RetrieveLibraryDetails:

    def __init__(self,session:Session,library_id:str) ->None:
        self.session=session
        self.library_id =library_id

    def get_library(self):
        library= self.session.query(Library).filter(Library.id == self.library_id).first()
        return library
    
    def run(self):
        return self.get_library()





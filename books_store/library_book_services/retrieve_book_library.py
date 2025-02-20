from sqlalchemy.orm import Session

from books_store.models import LibraryBooks
from books_store.schemas import RetrieveLibraryBookSchema

class RetrieveAllBooks:
    def __init__(self,library_id,session:Session,payload:RetrieveLibraryBookSchema) ->None:
        self.session=session
        self.payload=payload
        self.library_id=library_id

    def retrieve_all_books(self) ->None:
        return self.session.query(LibraryBooks).all()
    
    def run(self):
        self.retrieve_all_books()

    
    
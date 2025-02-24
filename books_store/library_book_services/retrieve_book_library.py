from sqlalchemy.orm import Session

from books_store.models import LibraryBooks
from books_store.schemas import RetrieveLibraryBookSchema

class RetrieveAllLibraryBooks:

    def __init__(self,library_id:str,session:Session) ->None:
        self.session=session
        self.library_id=library_id

    def retrieve_all_books(self) ->None:
        books = self.session.query(LibraryBooks).filter(LibraryBooks.library_id == self.library_id).all()
        return books
    
    def run(self):
        return self.retrieve_all_books()


#return library/{library_id}/books/count


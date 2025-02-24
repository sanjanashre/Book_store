from sqlalchemy.orm import Session

from books_store.models import LibraryBooks
from books_store.schemas import AddLibraryBookSchema

class AddLibraryBook:

    def __init__(self,book_id,session:Session,payload:AddLibraryBookSchema) ->None:
        self.session=session
        self.payload=payload
        self.book_id=book_id

    def add_library_book(self):
        library_book = LibraryBooks (
            id= self.payload.id ,
            library_id =self.payload.library_id,
            book_id = self.payload.book_id
        )

        self.session.add(library_book)
        self.session.refresh()
        return library_book
    
    def run(self):
        self.add_library_book()

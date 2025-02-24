from sqlalchemy.orm import Session

from books_store.models import LibraryBooks,Library
from books_store.schemas import AddLibraryBookSchema

class AddLibraryBook:

    def __init__(self,library_id,session:Session,payload:AddLibraryBookSchema) ->None: 
        self.session=session
        self.payload=payload
        self.library_id=library_id

    def validate_library(self):
        """Check if the library ID exists in the database."""
        return self.session.query(Library).filter(Library.id == self.library_id).first()

    def add_library_book(self):

        for book_id in self.payload.book_ids:
            library_book = LibraryBooks (
    
            library_id =self.library_id,
            book_id = book_id
             )

            self.session.add(library_book)
        self.session.commit()
        self.session.refresh(library_book)
        
    
    def run(self):
        return self.add_library_book()

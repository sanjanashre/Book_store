from sqlalchemy.orm import Session

from books_store.models import Library
from books_store.schemas import AddLibrarySchema


class AddLibrary:

<<<<<<< HEAD
    def __init__(self,session:Session,payload:AddLibrarySchema) ->None:
        """Constructor for Library
        """
        self.session=session
        self.payload=payload
    
    def add_library_run(self) ->None:
        library = Library (
            name = self.payload.name ,
            address_line_one =self.payload.address_line_one,
            address_line_two=self.payload.address_line_two,
            city = self.payload.city,
            state = self.payload.state,
            country = self.payload.country,
            zip_code= self.payload.zip_code  
            )
        
=======
    def __init__(self, session: Session, payload: AddLibrarySchema) -> None:
        """Constructor for Library"""
        self.session = session
        self.payload = payload

    def add_library_run(self) -> None:
        library = Library(
            id=self.payload.id,
            name=self.payload.name,
            address_line_one=self.payload.address_line_one,
            address_line_two=self.payload.address_line_two,
            city=self.payload.city,
            state=self.payload.state,
            country=self.payload.country,
            zip_code=self.payload.zip_code,
        )
>>>>>>> 1cef5bfda26d6bf4d2171ba84432584f7a69a179
        self.session.add(library)
        self.session.refresh()

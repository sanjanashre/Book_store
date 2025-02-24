from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from books_store.services.update_book import UpdateBookService
from books_store.database import get_db
from books_store.schemas import AddBookRequestSchema,BaseDetailSchema,RetrieveBooksSchema,BaseBookSchema,AddLibraryBookSchema, RetrieveLibraryBookSchema,LibraryRequestSchema,RetrieveLibrarySchema
from books_store.services.add_book import AddBookService
from books_store.services.retrieve_book import RetrieveBookDetails,RetrieveAllBooks
from books_store.services.delete_book import DeleteBook
from books_store.library_services.add_library import AddLibrary
from books_store.library_services.retrieve_library import RetrieveLibraryDetails
from books_store.library_book_services.add_book_library import AddLibraryBook
router = APIRouter()


@router.get("/books", response_model=List[RetrieveBooksSchema])
def read_books( db: Session = Depends(get_db)):
    """
    Retrieves all book entries from the database.

    This function handles the HTTP GET request to fetch all books stored in the database.
    If books are found, a list of book details is returned. If no books exist, an empty list is returned.

    Parameters:
        db (Session): The database session dependency used to interact with the database.

    Returns:
        List[RetrieveBooksSchema]: A list of response models containing the details of all books.
    """
    get_all_books = RetrieveAllBooks(session=db)
    return get_all_books.retrieve_all()


@router.post("/books", response_model=BaseBookSchema)
def create_new_book(payload:BaseBookSchema, db: Session = Depends(get_db)):
    """
    Creates a new book entry in the database using the provided payload data.

    This function is responsible for handling the HTTP POST request to create
    a new book. It utilizes a service layer to add the book to the database
    and commits the changes. If any error occurs during the database
    operation, it raises an HTTP exception.

    Parameters:
        payload (AddBookRequestSchema): The schema containing the data for
        the new book.
        db (Session): The database session dependency used to interact with
        the database.

    Raises:
        HTTPException: Raised when an error occurs while committing the
        transaction.

    Returns:
        BaseDetailSchema: A response model indicating the book has been
        successfully added.
    """
    add_book_service = AddBookService(session=db, payload=payload)
    new_book=add_book_service.add_book()
    return new_book



@router.put("/books/{book_id}", response_model=AddBookRequestSchema)
def update_book(book_id:str,payload: AddBookRequestSchema, db: Session = Depends(get_db)):
    """Updates an existing book entry in the database using the provided payload data.

    This function is responsible for handling the HTTP PUT/PATCH request to update
    an existing book. It retrieves the book by its ID, applies the necessary updates,
    and commits the changes. If the book is not found, or if an error occurs during 
    the update process, an HTTP exception is raised.

    Parameters:
        book_id (int): The unique identifier of the book to be updated.
        payload (ReceiveBooksSchema): The schema containing the updated data 
        for the book.
        db (Session): The database session dependency used to interact with
        the database.

    Raises:
        HTTPException: Raised when the book is not found or an error occurs 
        while committing the transaction.

    Returns:
        BaseDetailSchema: A response model indicating the book has been 
        successfully updated.
    """
    update_book_service = UpdateBookService(session=db, payload=payload, book_id=book_id)
    update_book_service.run()  

    return BaseDetailSchema(detail="Book updated successfully")   





@router.get("/books/{book_id}", response_model=RetrieveBooksSchema)
def get_book(book_id, db : Session = Depends(get_db)):
    """Retrieves a book entry from the database using the provided book ID.

    This function handles the HTTP GET request to fetch book details. It queries
    the database for the book based on the given ID. If the book is found, its 
    details are returned. If the book does not exist, an HTTP exception is raised.

    Parameters:
        book_id (int): The unique identifier of the book to be retrieved.
        db (Session): The database session dependency used to interact with
        the database.

    Raises:
        HTTPException: Raised when the book is not found.

    Returns:
        RetrieveBooksSchema: A response model containing the details of the 
        retrieved book.
    """

    retrieve_Book_Service = RetrieveBookDetails(session=db, book_id=book_id)
    return retrieve_Book_Service.run()






@router.delete("/books/{book_id}",response_model=BaseBookSchema )
def delete_book(book_id:str, db: Session = Depends(get_db)):
    """ Deletes a book entry from the database using the provided book ID.

    This function handles the HTTP DELETE request to remove a book from the database.
    It queries the database for the book based on the given ID. If the book is found,
    it is deleted from the database. If the book does not exist, an HTTP exception is raised.

    Parameters:
        book_id (int): The unique identifier of the book to be deleted.
        db (Session): The database session dependency used to interact with
        the database.

    Raises:
        HTTPException: Raised when the book is not found.

    Returns:
        RetrieveBooksSchema: A response model containing the details of the 
        deleted book."""
    
    delete_Book_Service = DeleteBook(session=db,book_id=book_id) 
    return delete_Book_Service.run()  




@router.get("/library/{library_id}",response_model=RetrieveLibrarySchema)
def retrieve_library(library_id:str,db:Session=Depends(get_db)):
    #retrieve details library details
   
    retrieve_library=RetrieveLibraryDetails(session=db,library_id=library_id)
    get_library =retrieve_library.run()  
    
    return get_library



@router.post("/library", response_model=LibraryRequestSchema)
def add_library(payload:LibraryRequestSchema,db:Session=Depends(get_db)):
    # Adds library details
    

    add_library=AddLibrary(session=db,payload=payload)
    new_library=add_library.add_library_run()


    try:
        db.commit()
    except:
        raise HTTPException(status_code=404,detail="Library is not added")
    
    return new_library

    
@router.post("/libraries/{library_id}/books",response_model=AddLibraryBookSchema)
def add_library_books(payload:AddLibraryBookSchema,db:Session=Depends(get_db)):
    add_library_book=AddLibraryBook(session=db,payload=payload),
    add_library_book.run()

    try:
        db.commit()
    except:
        raise HTTPException(status_code=404,detail="library not found")
    

@router.get("/libraries/{library_id}/books",response_model=list[RetrieveLibraryBookSchema])
def list_library_books(library_id:str,db:Session=Depends(get_db)):
    retrieve_library_book = RetrieveAllBooks(session=db ,library_id=library_id)
    return retrieve_library_book.run()


"""[
    {
        id: UUID
        book: RetrieveBooksSchema
    },
{
        id: UUID
        book: RetrieveBooksSchema
    },
{
        id: UUID
        book: RetrieveBooksSchema
    }
]"""
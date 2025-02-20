from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import session
from books_store.services.update_book import UpdateBookService
from books_store.database import get_db
from books_store.schemas import AddBookRequestSchema, BaseDetailSchema, \
    RetrieveBooksSchema, AddLibraryBookSchema, RetrieveLibraryBookSchema
from books_store.services.add_book import AddBookService
from books_store.services.retrieve_book import RetrieveBookDetails
from books_store.services.delete_book import DeleteBook
from books_store.schemas import AddLibrarySchema,RetrieveLibrarySchema
from books_store.library_services.add_library import AddLibrary
from books_store.library_services.retrieve_library import RetrieveLibraryDetails

router = APIRouter()


@router.get("/books", response_model=list[RetrieveBooksSchema])
def read_books(payload: RetrieveBooksSchema, db: session = Depends(get_db)):
    """
    Retrieves all book entries from the database.

    This function handles the HTTP GET request to fetch all books stored in the database.
    If books are found, a list of book details is returned. If no books exist, an empty list is returned.

    Parameters:
        db (Session): The database session dependency used to interact with the database.

    Returns:
        List[RetrieveBooksSchema]: A list of response models containing the details of all books.
    """
    get_all_books = RetrieveBookDetails(session=db,payload=payload)
    get_all_books.run()


@router.post("/books", response_model=AddBookRequestSchema)
def create_new_book(payload: AddBookRequestSchema, db: session = Depends(get_db)):
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
    add_book_service.add_book()

    try:
        db.commit()
    except Exception as e:
        raise HTTPException(
            detail="Something went wrong.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return BaseDetailSchema(detail="Book added successfully.")



@router.put("/books/{book_id}", response_model=AddBookRequestSchema)
def update_book(book_id,payload: AddBookRequestSchema, db: session = Depends(get_db)):
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
    update_book_service = UpdateBookService(session=db, payload=payload,book_id=book_id)
    update_book_service.run()
     
    try :
       db.commit 
    except :
       raise HTTPException(status_code= 404,detail="Book not found")
    
    return BaseDetailSchema(detail="Book updated")   

@router.get("/books/{book_id}", response_model=RetrieveBooksSchema)
def get_book(book_id,payload:RetrieveBooksSchema, db : session = Depends(get_db)):
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

    Retrieve_Book_Service = RetrieveBookDetails(session=db, payload=payload,book_id=book_id)
    Retrieve_Book_Service.run()




@router.delete("/books/{book_id}",response_model=RetrieveBooksSchema )
def delete_book(book_id,payload:RetrieveBookDetails, db: session = Depends(get_db)):
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
    try:
        Delete_Book_Service = DeleteBook(session=db, payload=payload,book_id=book_id) 
        Delete_Book_Service.run()  
        return {"Successfully deleted"}
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
    



@router.post("/library", response_model=AddLibrarySchema)
def add_library(payload:AddLibrarySchema,db:session=Depends(get_db)):
    """ Adds library details
    """

    add_library=AddLibrary(session=db,payload=payload)
    add_library.add_library_run()

    try:
        db.commit()
    except:
        raise HTTPException(status_code=404,detail="book is not added")


@router.post("/library",response_model=RetrieveLibrarySchema)
def retrieve_library(library_id,payload:RetrieveLibrarySchema,db:session=Depends(get_db)):
    """retrieve details library details
    """
    retrieve_library=RetrieveLibraryDetails(session=db,payload=payload,library_id=library_id)
    retrieve_library.run()

@router.post("/libraries/{library_id}/books",response_model=AddLibraryBookSchema)
def add_library_books():
    pass


@router.get("/libraries/{library_id}/books",response_model=list[RetrieveLibraryBookSchema])
def list_library_books():
    pass

[
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
]
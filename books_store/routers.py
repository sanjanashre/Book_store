from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import session

from books_store.database import get_db
from books_store.schemas import AddBookRequestSchema, BaseDetailSchema
from books_store.services.add_book import AddBookService

router = APIRouter()


@router.get("/books", response_model=list[schemas.BookResponse])
def read_books(db: session = Depends(get_db)):
    """List books"""
    books = crud.get_books(db)
    return [schemas.BookResponse.from_orm(book) for book in books]


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


@router.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: str, db: session = Depends(get_db)):
    """Retrieve book by ID"""
    return crud.get_book(db, book_id)


@router.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: str, book: schemas.BookCreate, db: session = Depends(get_db)):
    return crud.update_book(db, book_id, book)


@router.delete("/books/{book_id}", response_model=schemas.BookResponse)
def delete_book(book_id: str, db: session = Depends(get_db)):
    """Delete book"""
    book = crud.get_book(db, book_id)

    if book:
        crud.delete_book(db, book_id)
        return book
    return None

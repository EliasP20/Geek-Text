from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book import BookCreate, BookResponse
from app.services import book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/create-book", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book)

#@router.get("/book/{book_id}", response_model=BookResponse)
#def get_book(book_id: int, db: Session = Depends(get_db)):
#    return book_service.get_book(db, book_id)

#@router.get("/")
#def get_books(db: Session = Depends(get_db)):
#    return book_service.get_books(db)
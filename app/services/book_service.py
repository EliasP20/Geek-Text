from sqlalchemy.orm import Session
from app.models.book import Book
from decimal import Decimal
from app.schemas.book import BookCreate

def create_book(db: Session, book: BookCreate):
    book = Book(
        isbn=book.isbn,
        title=book.title,
        description=book.description,
        price=book.price,
        genre=book.genre,
        publisher=book.publisher,
        year_published=book.year_published,
        copies_sold=book.copies_sold,
        author_id=book.author_id,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
from sqlalchemy.orm import Session
from app.models.book import Book

def get_books_by_genre(db: Session, genre: str):
    return db.query(Book).filter(Book.genre == genre).all()

def get_top_sellers(db: Session):
    return (
        db.query(Book)
        .order_by(Book.copies_sold.desc())
        .limit(10)
        .all()
    )

def get_books_by_rating(db: Session, rating: float):
    return db.query(Book).filter(Book.rating >= rating).all()

def discount_books_by_publisher(db: Session, publisher: str, discount: float):
    books = db.query(Book).filter(Book.publisher == publisher).all()

    for book in books:
        book.price = book.price * (1 - discount / 100)

    db.commit()

from sqlalchemy.orm import Session
from app.models.book import Book

from sqlalchemy import func
from app.models.rating import Rating


def get_books_by_genre(db: Session, genre: str):
    return (
        db.query(Book)
        .filter(Book.genre == genre)
        .all()
    )

def get_top_sellers(db: Session):
    return (
        db.query(Book)
        .order_by(Book.copies_sold.desc())
        .limit(10)
        .all()
    )

def discount_books_by_publisher(db: Session, publisher: str, discount: float):
    books = (
        db.query(Book)
        .filter(Book.publisher == publisher)
        .all()
    )

    for book in books:
        book.price = book.price * (1 - discount / 100)

    db.commit()

def get_books_by_min_rating(db, min_rating: float):
    results = (
        db.query(
            Book,
            func.avg(Rating.rating).label("average_rating")
        )
        .join(Rating, Rating.book_id == Book.id)
        .group_by(Book.id)
        .having(func.avg(Rating.rating) >= min_rating)
        .all()
    )

    books = []
    for book, avg_rating in results:
        book.average_rating = round(avg_rating, 2)
        books.append(book)

    return books


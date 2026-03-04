from decimal import Decimal

from sqlalchemy.orm import Session
from app.models import Book, Author

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
    """
    Apply a discount to all books by the given publisher.

    Args:
        db: SQLAlchemy Session
        publisher: Publisher name
        discount: Discount percentage (e.g., 10 for 10%)
    """
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")

    # Convert discount percentage to Decimal once
    discount_factor = Decimal(1) - Decimal(discount) / Decimal(100)

    # Get all books by the publisher
    books = db.query(Book).filter(Book.publisher == publisher).all()

    for book in books:
        # Multiply Decimal price by Decimal discount factor
        book.price = book.price * discount_factor

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


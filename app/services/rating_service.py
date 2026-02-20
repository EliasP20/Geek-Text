from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.rating import Rating
from app.models.comment import Comment
from app.services.users_service import get_user_by_id


"""
rating_service.py

Contains all business logic related to ratings and comments.
Routers should call these functions instead of directly querying the database.
"""

USER_NOT_FOUND = "USER_NOT_FOUND"
INVALID_RATING = "INVALID_RATING"
EMPTY_TEXT = "EMPTY_TEXT"

def create_rating(db: Session, user_id: int, book_id: int, rating_value: int):
    """
        Creates a new rating for a book by a user.

        Args:
            db: Database session
            user_id: ID of the user submitting rating
            book_id: ID of the book being rated
            rating_value: Integer rating (1-5)

        Returns:
            Newly created Rating object
    """
    
    ##Check if User exists
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(USER_NOT_FOUND)
    
     ##Check if the rating is within the range:
    if rating_value < 0 or rating_value > 5:
        raise ValueError (INVALID_RATING)
    

    rating = Rating(user_id=user_id, book_id=book_id, rating=rating_value)
    db.add(rating)
    db.commit()
    db.refresh(rating)
    return rating



def create_comment(db: Session, user_id: int, book_id: int, text: str):
    """
        Creates a new comment for a book by a user.

        Args:
            db: Database session
            user_id: ID of the user submitting comment
            book_id: ID of the book being commented
            text: description of the comment made by the user

        Returns:
            Newly created Comment object
    """
     ##Check if User exists
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(USER_NOT_FOUND)
    
    ##Check if text is not empty
    if not text or text.strip() == "":
        raise ValueError(EMPTY_TEXT)

    comment = Comment(user_id=user_id, book_id=book_id, comment=text)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comments_by_book(db: Session, book_id: int):
    """
        Retrieve all comments from a specific book

        Args:
            db: Database session
            book_id: ID of the targeted book

        Returns:
            List of Comment objects from an specific book or null if no book is found
    """
    return db.query(Comment).filter(Comment.book_id == book_id).all()




def get_average_rating(db: Session, book_id: int):
    """
        Calculates the average rating from an specific book

        Args:
            db: Database session
            book_id: ID of the book to calculate rating

        Returns:
            The average rating of the book or 0 if its not found
    """
    avg = db.query(func.avg(Rating.rating)).filter(Rating.book_id == book_id).scalar()
    return round(avg, 2) if avg else 0



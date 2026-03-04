from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.rating import Rating
from app.models.comment import Comment
from app.services.users_service import get_user_by_id
from typing import cast

"""
rating_service.py

Contains all business logic related to ratings and comments.
Routers should call these functions instead of directly querying the database.
"""

USER_NOT_FOUND = "USER_NOT_FOUND"
EMPTY_TEXT = "EMPTY_TEXT"

def create_rating(db: Session, user_id: int, book_id: int, rating_value: int):
    ##Check if User exists
    validate_user(db, user_id)
    
    #If the rating already exists it will override the previous rating
    existing_rating = db.query(Rating).filter(
        Rating.user_id == user_id,
        Rating.book_id == book_id,
    ).first()

    if existing_rating:
        cast(Rating, existing_rating).rating = rating_value # type:ignore[attr-defined]
        db.commit()
        db.refresh(existing_rating)
        return existing_rating

    rating = Rating(user_id=user_id, book_id=book_id, rating=rating_value)
    db.add(rating)
    db.commit()
    db.refresh(rating)
    return rating



def create_comment(db: Session, user_id: int, book_id: int, text: str):
     ##Check if User exists
    validate_user(db, user_id)
    
    ##Check if text is not empty
    if not text.strip():
        raise ValueError(EMPTY_TEXT)

    comment = Comment(
        user_id=user_id,
        book_id=book_id,
        comment=text
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_book_comments(db: Session, book_id: int):
    return db.query(Comment).filter(Comment.book_id == book_id).all()




def get_average_rating(db: Session, book_id: int):
    avg = db.query(func.avg(Rating.rating))\
    .filter(Rating.book_id == book_id)\
    .scalar()
    
    return round(float(avg), 2) if avg else 0.0


def validate_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(USER_NOT_FOUND)
    return user


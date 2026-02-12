from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

"""
Rating model

Represents a user's rating for a specific book.
Each user can rate a book, and ratings are used to calculate averages.
"""

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to user who made the rating
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    # Foreign key to rated book
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))

    #Rating value from 1 to 5
    rating = Column(Integer, nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .database import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    rating = Column(Integer)

    book = relationship("Book", back_populates="ratings")

    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 5"),
    )

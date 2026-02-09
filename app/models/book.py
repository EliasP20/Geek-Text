from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Book(Base):
    __tablename__ = "books"



    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String(20), nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    genre = Column(String(100))
    publisher = Column(String(100))
    year_published = Column(Integer)
    copies_sold = Column(Integer, default=0)

    author_id = Column(
        Integer,
        ForeignKey("authors.id", ondelete="SET NULL"),
        nullable=True
    )

    author = relationship("Author", back_populates="book")

    ratings = relationship("Rating", back_populates="book")

from sqlalchemy import Column, Integer, String, Float, DECIMAL
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    author = Column(String(255))
    genre = Column(String(100))
    publisher = Column(String(255))
    price = Column(DECIMAL(10, 2))
    rating = Column(Float)
    copies_sold = Column(Integer)

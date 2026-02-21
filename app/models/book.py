from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String(20), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    genre = Column(String(100), nullable=True)
    publisher = Column(String(100), nullable=True)
    year_published = Column(Integer, nullable=True)
    copies_sold = Column(Integer, nullable=True)
    author_id = Column(Integer, nullable=True)

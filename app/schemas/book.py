from decimal import Decimal

from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    isbn: str
    title: str
    description: Optional[str] = None
    price: Decimal
    genre: Optional[str] = None
    publisher: Optional[str] = None
    year_published: Optional[int] = None
    copies_sold: Optional[int] = None
    author_id: Optional[int] = None

class BookResponse(BaseModel):
    id: int
    isbn: str
    title: str
    description: Optional[str]
    price: Decimal
    genre: Optional[str]
    publisher: Optional[str]
    year_published: Optional[int]
    copies_sold: int
    author_id: Optional[int]

    average_rating: Optional[float] = None

    class Config:
        orm_mode = True

from pydantic import BaseModel
from decimal import Decimal
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
    description: Optional[str] = None
    price: float
    genre: Optional[str] = None
    publisher: Optional[str] = None
    year_published: Optional[int] = None
    copies_sold: int
    author_id: Optional[int] = None

    class Config:
        from_attributes = True
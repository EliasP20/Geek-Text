from pydantic import BaseModel
from typing import Optional

class BookResponse(BaseModel):
    id: int
    isbn: str
    title: str
    description: Optional[str]
    price: float
    genre: Optional[str]
    publisher: Optional[str]
    year_published: Optional[int]
    copies_sold: int
    author_id: Optional[int]
    average_rating: float | None = None
    class Config:
        orm_mode = True

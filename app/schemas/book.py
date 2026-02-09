from pydantic import BaseModel

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    publisher: str
    price: float
    rating: float
    copies_sold: int

    class Config:
        orm_mode = True

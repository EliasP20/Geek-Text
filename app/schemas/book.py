from decimal import Decimal

from pydantic import BaseModel
from typing import Optional

class BookResponse(BaseModel):
    id: int
    title: str
    price: Decimal
    genre: Optional[str]
    publisher: Optional[str]

    class Config:
        orm_mode = True

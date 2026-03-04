from pydantic import BaseModel
from app.schemas.book import BookResponse

class CartItemRead(BaseModel):
    quantity: int
    book: BookResponse

    class Config:
        from_attributes = True

class CartResponse(BaseModel):
    user_id: int
    user_name: str
    items: list[CartItemRead]

    class Config:
        from_attributes = True

class CartSubtotalResponse(BaseModel):
    user_id: int
    subtotal: float
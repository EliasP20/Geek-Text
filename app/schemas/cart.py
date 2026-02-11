from pydantic import BaseModel
from app.schemas.book import BookResponse

# Used to read the items within a given cart, used in tandem with other schemas
class CartItemRead(BaseModel):
    quantity: int
    book: BookResponse

    class Config:
        from_attributes = True

# Used for 'Retrieve the list of book(s) in the user's shopping cart'
class CartResponse(BaseModel):
    user_id: int
    user_name: str # Matches the 'user_name' variable in your router
    items: list[CartItemRead] # Renamed 'books' to 'items' to match your model

    class Config:
        from_attributes = True

# Used for 'Retrieve the subtotal price'
class CartSubtotalResponse(BaseModel):
    user_id: int
    subtotal: float
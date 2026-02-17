from pydantic import BaseModel

class WishlistCreate(BaseModel):
    user_id: int
    name: str


class AddBookToWishlist(BaseModel):
    wishlist_id: int
    book_id: int

from pydantic import BaseModel

class RatingCreate(BaseModel):
    user_id: int
    book_id: int
    rating: int


class RatingResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    rating: int

    class Config:
        from_attributes = True

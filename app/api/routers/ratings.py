from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.rating import RatingCreate, RatingResponse
from app.schemas.comment import CommentCreate, CommentResponse
from app.services import rating_service
from fastapi import HTTPException


router = APIRouter(prefix="/ratings", tags=["Ratings & Comments"])


@router.post("/rate", response_model=RatingResponse)
def add_rating(data: RatingCreate, db: Session = Depends(get_db)):
    try: 
        return rating_service.create_rating(db, data.user_id, data.book_id, data.rating)
    except ValueError as e:
        if str(e) == rating_service.USER_NOT_FOUND:
            raise HTTPException(status_code=404, detail="User not found")
        
        if str(e) == rating_service.INVALID_RATING:
            raise HTTPException(status_code=400, detail="Rating must be between 0 and 5")
        
        raise HTTPException(status_code=500, detail="Unexpected error")
        


@router.post("/comment", response_model=CommentResponse)
def add_comment(data: CommentCreate, db: Session = Depends(get_db)):
    try:
        return rating_service.create_comment(db, data.user_id, data.book_id, data.comment)
    except ValueError as e:
        if str(e) == rating_service.USER_NOT_FOUND:
            raise HTTPException(status_code=404, detail="User not found")
        
        if str(e) == rating_service.EMPTY_TEXT:
            raise HTTPException(status_code=400, detail="The comment should not be empty")
        
        raise HTTPException(status_code=500, detail="Unexpected error")



@router.get("/comments/{book_id}", response_model=list[CommentResponse])
def get_comments(book_id: int, db: Session = Depends(get_db)):
    return rating_service.get_comments_by_book(db, book_id)


@router.get("/average/{book_id}")
def get_avg_rating(book_id: int, db: Session = Depends(get_db)):
    avg = rating_service.get_average_rating(db, book_id)
    return {"book_id": book_id, "average_rating": avg}

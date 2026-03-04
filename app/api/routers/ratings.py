from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.rating import RatingCreate, RatingResponse
from app.schemas.comment import CommentCreate, CommentResponse
from app.services import rating_service


router = APIRouter(
    prefix="/books",
    tags=["Ratings & Comments"]
)

@router.post("/{book_id}/ratings", response_model=RatingResponse)
def add_rating(
    book_id: int,
    data: RatingCreate,
    db: Session = Depends(get_db)
):
    try:
        return rating_service.create_rating(
            db,
            data.user_id,
            book_id,
            data.rating
        )

    except ValueError as e:
        if str(e) == rating_service.USER_NOT_FOUND:
            raise HTTPException(404, "User not found")

        raise HTTPException(500, "Unexpected error")
    

@router.post("/{book_id}/comments", response_model=CommentResponse)
def add_comment(
    book_id: int,
    data: CommentCreate,
    db: Session = Depends(get_db)
):
    try:
        return rating_service.create_comment(
            db,
            data.user_id,
            book_id,
            data.comment
        )

    except ValueError as e:
        if str(e) == rating_service.USER_NOT_FOUND:
            raise HTTPException(404, "User not found")

        if str(e) == rating_service.EMPTY_TEXT:
            raise HTTPException(400, "Comment cannot be empty")

        raise HTTPException(500, "Unexpected error")
    

@router.get("/{book_id}/comments",
            response_model=list[CommentResponse])
def get_comments(
    book_id: int,
    db: Session = Depends(get_db)
):
    return rating_service.get_book_comments(db, book_id)


@router.get("/{book_id}/ratings/average")
def get_average_rating(
    book_id: int,
    db: Session = Depends(get_db)
):
    avg = rating_service.get_average_rating(db, book_id)

    return {
        "book_id": book_id,
        "average_rating": avg
    }
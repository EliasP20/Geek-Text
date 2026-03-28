from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.author import AuthorCreate, AuthorResponse
from app.services import author_service

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/create-author", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return author_service.create_author(db, author)
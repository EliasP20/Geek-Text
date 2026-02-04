from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter(tags=["Users"])

@router.get("/users/{username}", response_model=UserResponse)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

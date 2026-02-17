from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from app.services import users_service

router = APIRouter(tags=["Users"])


@router.get("/users/{username}", response_model=UserResponse)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = users_service.get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if users_service.username_exists(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    users_service.create_user(db, user)
    return Response(status_code=201)  # truly empty body


@router.patch("/users/{username}", status_code=204)
def update_user(username: str, updates: UserUpdate, db: Session = Depends(get_db)):
    user = users_service.get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    users_service.update_user(db, user, updates)
    return Response(status_code=204)

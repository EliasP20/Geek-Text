from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserCreate, UserUpdate

router = APIRouter(tags=["Users"])

@router.get("/users/{username}", response_model=UserResponse)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/users", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        username=user.username,
        password=user.password,
        name=user.name,
        email=user.email,
        address=user.address
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return


@router.patch("/users/{username}", status_code=204)
def update_user(username: str, updates: UserUpdate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if updates.password is not None:
        user.password = updates.password

    if updates.name is not None:
        user.name = updates.name

    if updates.address is not None:
        user.address = updates.address

    db.commit()

    return
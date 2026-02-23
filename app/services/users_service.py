from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def username_exists(db: Session, username: str) -> bool:
    return db.query(User).filter(User.username == username).first() is not None


def create_user(db: Session, data: UserCreate) -> User:
    new_user = User(
        username=data.username,
        password=data.password,   # later: hash this
        name=data.name,
        email=data.email,
        address=data.address,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user: User, updates: UserUpdate) -> User:
    # only update fields that were provided
    if updates.password is not None:
        user.password = updates.password
    if updates.name is not None:
        user.name = updates.name
    if updates.address is not None:
        user.address = updates.address

    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

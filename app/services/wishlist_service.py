from sqlalchemy.orm import Session
from app.models.wishlist import Wishlist
from app.models.wishlist_item import WishlistItem
from app.services.users_service import get_user_by_id

USER_NOT_FOUND = "USER NOT FOUND"
EMPTY_TEXT = "EMPTY TEXT"
WISHLIST_NOT_FOUND = "WISHLIST NOT FOUND"
BOOK_NOT_IN_WISHLIST = "BOOK_NOT_IN_WISHLIST"
MAX_WISHLISTS_REACHED = "MAX WISHLISTS REACHED"
WISHLIST_ALREADY_EXISTS = "WISHLIST_ALREADY_EXISTS"
BOOK_ALREADY_IN_WISHLIST = "BOOK ALREADY IN WISHLIST"

def create_wishlist(db: Session, user_id: int, name: str):
    #Check if User exists
    validate_user(db, user_id)

    #Check if tha name is not emty
    if not name or name.strip() == "":
        raise ValueError(EMPTY_TEXT)
    
    
    # Max 3 wishlists per user
    wishlist_count = db.query(Wishlist)\
        .filter(Wishlist.user_id == user_id)\
        .count()

    if wishlist_count >= 3:
        raise ValueError(MAX_WISHLISTS_REACHED)

    wishlist = Wishlist(user_id=user_id, name=name)

    #Check if wishilist already exists
    duplicated_wishlist(db, user_id, name)
    
    db.add(wishlist)
    db.commit()
    db.refresh(wishlist)
    return wishlist


def add_book_to_wishlist(db: Session, wishlist_id: int, book_id: int):
    # Check if wishlist exists
    validate_wishlist(db, wishlist_id)

    #Check if the book is already in the wishlist
    existing_item = db.query(WishlistItem).filter(
        WishlistItem.wishlist_id == wishlist_id,
        WishlistItem.book_id == book_id
    ).first()

    if existing_item:
        raise ValueError(BOOK_ALREADY_IN_WISHLIST)

    item = WishlistItem(wishlist_id=wishlist_id, book_id=book_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_user_wishlists(db: Session, user_id: int):
    validate_user(db, user_id)
    return db.query(Wishlist).filter(Wishlist.user_id == user_id).all()


def get_books_in_wishlist(db: Session, wishlist_id: int):
    validate_wishlist(db, wishlist_id)
    return db.query(WishlistItem).filter(WishlistItem.wishlist_id == wishlist_id).all()


def remove_book(db: Session, wishlist_id: int, book_id: int):
    #Check if Wishlist exists
    validate_wishlist(db, wishlist_id)
    
    item = db.query(WishlistItem).filter(
        WishlistItem.wishlist_id == wishlist_id,
        WishlistItem.book_id == book_id
    ).first()



    if not item:
        raise ValueError(BOOK_NOT_IN_WISHLIST)
    
    db.delete(item)
    db.commit()


def get_wishlist_by_id(db: Session, wishlist_id: int) -> Wishlist | None:
    return db.query(Wishlist).filter(Wishlist.id == wishlist_id).first()


def validate_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(USER_NOT_FOUND)
    return user

def validate_wishlist(db: Session, wishlist_id: int) -> Wishlist | None:
    wishlist = get_wishlist_by_id(db, wishlist_id)
    if not wishlist:
        raise ValueError(WISHLIST_NOT_FOUND)
    return wishlist

def duplicated_wishlist(db: Session, user_id, name: str) -> Wishlist | None:
    existing = db.query(Wishlist).filter(
        Wishlist.user_id == user_id,
        Wishlist.name == name
    ).first()

    if existing:
        raise ValueError(WISHLIST_ALREADY_EXISTS)
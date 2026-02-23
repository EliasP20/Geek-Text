from sqlalchemy.orm import Session
from app.models.wishlist import Wishlist
from app.models.wishlist_item import WishlistItem


def create_wishlist(db: Session, user_id: int, name: str):
    wishlist = Wishlist(user_id=user_id, name=name)
    db.add(wishlist)
    db.commit()
    db.refresh(wishlist)
    return wishlist


def add_book_to_wishlist(db: Session, wishlist_id: int, book_id: int):
    item = WishlistItem(wishlist_id=wishlist_id, book_id=book_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_user_wishlists(db: Session, user_id: int):
    return db.query(Wishlist).filter(Wishlist.user_id == user_id).all()


def get_books_in_wishlist(db: Session, wishlist_id: int):
    return db.query(WishlistItem).filter(WishlistItem.wishlist_id == wishlist_id).all()


def remove_book(db: Session, wishlist_id: int, book_id: int):
    item = db.query(WishlistItem).filter(
        WishlistItem.wishlist_id == wishlist_id,
        WishlistItem.book_id == book_id
    ).first()

    if item:
        db.delete(item)
        db.commit()

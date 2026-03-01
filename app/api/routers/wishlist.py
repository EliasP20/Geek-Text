from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.wishlist import WishlistCreate, AddBookToWishlist
from app.services import wishlist_service

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])

#Create wishlist
@router.post("/create")
def create_wishlist(data: WishlistCreate, db: Session = Depends(get_db)):
    return wishlist_service.create_wishlist(db, data.user_id, data.name)


#Add a Book to a wishlist
@router.post("/add-book")
def add_book(data: AddBookToWishlist, db: Session = Depends(get_db)):
    return wishlist_service.add_book_to_wishlist(db, data.wishlist_id, data.book_id)


#Get a user's list
@router.get("/user/{user_id}")
def get_user_lists(user_id: int, db: Session = Depends(get_db)):
    return wishlist_service.get_user_wishlists(db, user_id)


#Get Books from a wishlist
@router.get("/{wishlist_id}")
def get_books(wishlist_id: int, db: Session = Depends(get_db)):
    return wishlist_service.get_books_in_wishlist(db, wishlist_id)


#Remove a Book from a wishlist
@router.delete("/remove/{wishlist_id}/{book_id}")
def remove_book(wishlist_id: int, book_id: int, db: Session = Depends(get_db)):
    wishlist_service.remove_book(db, wishlist_id, book_id)
    return {"message": "Book removed"}

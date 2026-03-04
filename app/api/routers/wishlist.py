from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.wishlist import (
    WishlistCreate, 
    WishlistResponse,
    WishlistItemResponse,
    AddBookToWishlist
)
from app.services import wishlist_service

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])

#Create wishlist
@router.post("/", response_model=WishlistResponse)
def create_wishlist(data: WishlistCreate, db: Session = Depends(get_db)):
    try:
        return wishlist_service.create_wishlist(
            db,
            data.user_id,
            data.name
        )

    except ValueError as e:

        if str(e) == wishlist_service.USER_NOT_FOUND:
            raise HTTPException(404, "User not found")

        if str(e) == wishlist_service.EMPTY_TEXT:
            raise HTTPException(400, "Wishlist name cannot be empty")

        if str(e) == wishlist_service.MAX_WISHLISTS_REACHED:
            raise HTTPException(400, "User can only have 3 wishlists")

        raise HTTPException(500, "Unexpected error")


#Add a Book to a wishlist
@router.post("/add-book")
@router.post("/items", response_model=WishlistItemResponse)
def add_book(data: AddBookToWishlist, db: Session = Depends(get_db)):
    try:
        return wishlist_service.add_book_to_wishlist(
            db,
            data.wishlist_id,
            data.book_id
        )

    except ValueError as e:

        if str(e) == wishlist_service.WISHLIST_NOT_FOUND:
            raise HTTPException(404, "Wishlist not found")
        
        if str(e) == wishlist_service.BOOK_ALREADY_IN_WISHLIST:
            raise HTTPException(
                status_code=400,
                detail="Book already exists in wishlist"
            )

        raise HTTPException(500, "Unexpected error")


#Get a user's list
@router.get("/user/{user_id}", response_model=list[WishlistResponse])
def get_user_lists(user_id: int, db: Session = Depends(get_db)):
    try:
        return wishlist_service.get_user_wishlists(db, user_id)

    except ValueError:
        raise HTTPException(404, "User not found")


#Get Books from a wishlist
@router.get("/{wishlist_id}", response_model=list[WishlistItemResponse])
def get_books(wishlist_id: int, db: Session = Depends(get_db)):
    try:
        return wishlist_service.get_books_in_wishlist(db, wishlist_id)

    except ValueError:
        raise HTTPException(404, "Wishlist not found")


#Remove a Book from a wishlist
@router.delete("/{wishlist_id}/items/{book_id}")
def remove_book(
    wishlist_id: int,
    book_id: int,
    db: Session = Depends(get_db)
):
    try:
        wishlist_service.remove_book(db, wishlist_id, book_id)
        return {"message": "Book removed successfully"}

    except ValueError:
        raise HTTPException(404, "Item not found")
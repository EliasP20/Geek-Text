from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.deps import get_db
from app.services import cart_service
from app.schemas.cart import CartResponse

router = APIRouter(prefix="/cart", tags=["Shopping Cart"])

@router.get("/subtotal/{user_id}")
def get_cart_subtotal(user_id: int, db: Session = Depends(get_db)):
    subtotal = cart_service.calculate_subtotal(db, user_id)
    return {"user_id": user_id, "subtotal": subtotal}

@router.get("/items/{user_id}", response_model=CartResponse)
def list_cart_items(user_id: int, db: Session = Depends(get_db)):
    cart = cart_service.get_user_cart(db, user_id)

    query = text("SELECT username FROM users WHERE id = :uid")
    result = db.execute(query, {"uid": user_id}).fetchone()
    user_name = result[0] if result else "Unknown User"

    aggregated_items = {}
    for item in cart.items:
        if item.book_id in aggregated_items:
            # Add to the existing quantity instead of making a new row, accounts for duplicate database entries
            aggregated_items[item.book_id].quantity += item.quantity
        else:
            # First time seeing this book, add it to our dictionary
            aggregated_items[item.book_id] = item

    return {
        "user_id": user_id,
        "user_name": user_name,
        "items": list(aggregated_items.values())
        }
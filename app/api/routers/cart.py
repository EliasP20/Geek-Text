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

    return {
        "user_id": user_id,
        "user_name": user_name,
        "items": cart.items
        }
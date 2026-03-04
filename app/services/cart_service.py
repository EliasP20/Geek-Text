from decimal import Decimal
from sqlalchemy.orm import Session
from app.models.cart import ShoppingCart

def get_user_cart(db: Session, user_id: int):
    # Stores the first cart found in the database into 'cart' variable
    cart = db.query(ShoppingCart).filter(ShoppingCart.user_id == user_id).first()
    
    # If there is no cart tied to the user it will add an empty cart
    if not cart:
        cart = ShoppingCart(user_id=user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart # cart.items will be [] at this point

def calculate_subtotal(db: Session, user_id: int):
    # Retrieves the user's cart
    cart = get_user_cart(db, user_id)

    # Calculates the subtotal by summing up the price of each cart item (uses book price * book quantity)
    subtotal = Decimal('0.00')
    for item in cart.items:
        subtotal += item.book.price * item.quantity
    return subtotal
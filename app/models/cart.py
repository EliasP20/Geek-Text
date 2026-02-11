from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base

class ShoppingCart(Base):
    __tablename__ = "shopping_carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    
    items = relationship("CartItem", 
                         back_populates="cart", 
                         cascade="all, delete-orphan", 
                         order_by="desc(CartItem.cart_id)")

class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("shopping_carts.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    quantity = Column(Integer, default=1)

    cart = relationship("ShoppingCart", back_populates="items")
    book = relationship("Book")
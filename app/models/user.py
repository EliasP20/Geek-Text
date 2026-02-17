from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)   # stored in DB, but we won't return it
    name = Column(String(100))
    email = Column(String(100))
    address = Column(String(255))

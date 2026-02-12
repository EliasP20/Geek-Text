from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

"""
database.py

Handles the database connection to MySQL using SQLAlchemy.
Creates the engine, session factory, and Base class for models.

All routers use get_db() dependency to interact with the database.
"""


# Change just password
DB_USER = "root"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "geek_text"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency used in FastAPI routes to get a DB session
# Automatically opens and closes the connection per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

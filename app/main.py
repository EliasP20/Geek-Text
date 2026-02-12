from fastapi import FastAPI
from app.database import Base, engine

# import routers
from app.api.routers import wishlist

# create app
app = FastAPI(title="Geek Text API")

# connect router
app.include_router(wishlist.router)

# ensure detected tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Geek Text API running"}


@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as conn:
            return {"db": "connected"}
    except Exception as e:
        return {"db": "failed", "error": str(e)}

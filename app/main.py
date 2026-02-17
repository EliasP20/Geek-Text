from fastapi import FastAPI
from app.database import Base, engine
from app.api.routers.users import router as users_router
from app.api.routers.ratings import router as ratings_router
from app.api.routers.wishlist import router as wishlists_router

app = FastAPI(title="Geek Text API")

app.include_router(users_router)
app.include_router(ratings_router)
app.include_router(wishlists_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Geek Text API running"}

@app.get("/health")
def health():
    try:
        with engine.connect() as conn:
            return {"status": "ok"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}


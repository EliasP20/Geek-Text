from fastapi import FastAPI
from app.database import Base, engine
from app.api.routers import wishlist_router

app = FastAPI(title="Geek Text API")

app.include_router(wishlist_router.router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Geek Text API running"}


@app.get("/health")
def test_db():
    try:
        with engine.connect() as conn:
            return {"status": "ok"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

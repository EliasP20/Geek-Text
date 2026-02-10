from fastapi import FastAPI
from app.database import Base, engine

# import models
import app.models.rating
import app.models.comment

# import routers
from app.api.routers import ratings

# create app
app = FastAPI(title="Geek Text API")

# connect routers
app.include_router(ratings.router)

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

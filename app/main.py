from fastapi import FastAPI
from app.api.routers import books

app = FastAPI(title="Geek Text API")

app.include_router(books.router)

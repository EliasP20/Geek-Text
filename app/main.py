from fastapi import FastAPI
from app.api.routers import cart

app = FastAPI(title="Geek Text API")

app.include_router(cart.router)

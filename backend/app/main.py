# app/main.py

from fastapi import FastAPI
from app.routers import user
from app.auth import routes as auth_routes

app = FastAPI()

app.include_router(user.router)
app.include_router(auth_routes.router)
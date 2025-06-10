#auth/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app import models
from app.auth.security import verify_password
from app.auth.jwt import create_access_token
from datetime import timedelta

router = APIRouter(prefix="/login", tags=["auth"])

@router.post("/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}

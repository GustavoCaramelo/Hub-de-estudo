from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.auth.jwt import verify_token
from app import models
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Não autorizado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = verify_token(token)
    if not payload or "sub" not in payload:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.email == payload["sub"]).first()
    if not user:
        raise credentials_exception

    return user

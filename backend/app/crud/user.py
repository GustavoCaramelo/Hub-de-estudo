# app/crud/user.py

from sqlalchemy.orm import Session
from app import models, schemas
from app.models import user as models
from app.schemas import user as schemas
from app.auth.security import hash_password
from fastapi import HTTPException
from app.schemas.user import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.user.User).filter(models.user.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.user.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> models.User:
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")
    
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
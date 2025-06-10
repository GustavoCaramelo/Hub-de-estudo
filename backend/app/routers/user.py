from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.dependencies import get_current_user
from app.crud import user as crud
from app.schemas import user as user_schema

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user=user)

@router.get("/", response_model=list[user_schema.User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: user_schema.User = Depends(get_current_user)
):
    return crud.get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=user_schema.User)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: user_schema.User = Depends(get_current_user)
):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=user_schema.User)
def update_user(
    user_id: int,
    user: user_schema.UserUpdate,
    db: Session = Depends(get_db),
    current_user: user_schema.User = Depends(get_current_user)
):
    updated_user = crud.update_user(db, user_id=user_id, user_data=user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=user_schema.User)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: user_schema.User = Depends(get_current_user)
):
    deleted_user = crud.delete_user(db, user_id=user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user

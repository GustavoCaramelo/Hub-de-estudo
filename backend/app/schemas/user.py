# app/schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
        
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
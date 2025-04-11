import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#defining the Schema for user signup
from models.user import User
from db.session import engine
from pydantic import BaseModel, EmailStr 
from core.config import settings

class UserCreation(BaseModel):
    Name: str
    Email: EmailStr
    Password: str
    Mobile: str
    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    Name: str
    Email: EmailStr
    Mobile: str
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    Email: EmailStr
    Password: str
    class Config:
        orm_mode = True

# class UserProfile(BaseModel,UserCreation):
     

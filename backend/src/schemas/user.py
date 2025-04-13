import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#defining the Schema for user signup
from models.user import User
from db.session import engine
from pydantic import BaseModel, EmailStr 
from core.config import settings
from fastapi import UploadFile
from typing import Optional

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
     
class ProfileSchema(BaseModel):
    Name : str
    Email : str
    City: Optional[str]
    States: Optional[str]
    Country: Optional[str]
    ResumeUploaded: bool = False
    Resume: Optional[str]
    ProfileImage: Optional[str]
    LinkedinId = Optional[str]
    GithubId = Optional[str]
    CodingProfiles = Optional[str] 
    SkillSet = Optional[str]
    YearsOfExperience = Optional[int]
    DesiredRole = Optional[str]



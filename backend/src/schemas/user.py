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
    City: Optional[str] = None
    States: Optional[str] = None
    Country: Optional[str] = None
    ResumeUploaded: bool = False 
    Resume: Optional[UploadFile] = None
    ProfileImage: Optional[str] = None
    LinkedinId : Optional[str] = None
    GithubId : Optional[str] = None
    CodingProfiles : Optional[str] = None 
    SkillSet : Optional[str] = None
    YearsOfExperience : Optional[int] = None
    DesiredRole : Optional[str] = None

    class Config: 
        orm_mode = True
        model_config = {
            "form_attributes": True
        }

import os 
import sys 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schemas.user import UserResponse, UserLogin, ProfileSchema
from models.user import User
from pydantic import EmailStr
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from db.session import get_db
from sqlalchemy.orm import Session

profileRouter = APIRouter()
@profileRouter.get('/profile/{user_email_id}')
def getprofile(user_email_id: EmailStr, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email_id).first()
    if not user:
        raise HTTPException(status_code=404, detail={"error": "User not Found"})
    ProfileResponse = ProfileSchema(Name=user.name,Email=user.email)
    response = {
        ProfileResponse.Name,
        ProfileResponse.Email,
        ProfileResponse.City,
        ProfileResponse.States,
        ProfileResponse.Country,
        ProfileResponse.Resume,
        ProfileResponse.ProfileImage,
        ProfileResponse.LinkedinId,
        ProfileResponse.GithubId,
        ProfileResponse.CodingProfiles,
        ProfileResponse.SkillSet,
        ProfileResponse.DesiredRole
    }
    return{f"{response} \n We are still working on User Profile redirect to localhost:8000/jobs "}

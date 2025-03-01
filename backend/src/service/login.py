import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from sqlalchemy.orm import Session
from schemas.user import UserCreation, UserLogin
from middleware.tokengenerator import verify_password, hashingofpassword
from core.config import settings

def Login(db: Session,Loginfeature: UserLogin):
    user = db.query(User).filter(User.email == Loginfeature.Email).first()
    if user:
        ## first we will pass the password of DB
        ## then we will pass the password user gave us
        if not verify_password(user.password, Loginfeature.Password):
            return {"response model": "Incorrect Password"}
        else:
            return {"response model": "Login Successfull"}
    else:
         return {"response message": "User not Found"}

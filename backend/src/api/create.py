import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import   APIRouter, HTTPException, Depends
from schemas.user import UserCreation, UserResponse
from service.signup import signup
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
router = APIRouter()

@router.post('/signup/', response_model=UserResponse )
def newuser(createUser: UserCreation, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == createUser.Email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with that email id already exist")
    
    newuser = signup.create_User(db , createUser)

    return newuser
   
    # if confirmpassword != password:
    #     Response({"response message: Make sure password field and confirm password should be same "})

    

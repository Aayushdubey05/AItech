import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user import User
from sqlalchemy.orm import Session
from db.session import engine, get_db, SessionLocal
from schemas.user import UserCreation 
from middleware.tokengenerator import hashingofpassword, verify_password

class signup:
    @staticmethod
    def create_User(db: Session, user_data: UserCreation):
        new_user = User(
            name = user_data.Name,
            Email = user_data.Email,
            Mobile = user_data.Mobile,
            Password = hashingofpassword(user_data.Password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
        

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user import user
from db.session import engine, get_db
from schemas.user import UserCreation 
from middleware.tokengenerator import hashingofpassword, verify_password

user = next(get_db()) 
class signup():
    @staticmethod
    async def create_user(usercreate: UserCreation):
        user.Name = usercreate.Name
        user.Email = usercreate.Email
        user.Mobile = usercreate.Mobile

        user.Password = hashingofpassword(usercreate.Password)

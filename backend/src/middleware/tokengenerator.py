##########   This is whole security creation ######### 
import os 
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import logging
from db.session import engine, get_db
from core.config import settings
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import bcrypt  #Avoid this underline problem its an glitch in the editor
from pydantic import EmailStr
import jwt #Avoid this underline problem its an glitch in the editor

## Will call this to apply SHA256 on password and this will return the hashed password to store in database
## Will not save this on redis type DB
## it is going to be used when user will signup


# logging.basicConfig(level=logging.DEBUG)
def hashingofpassword(password: str):
    salt = bcrypt.gensalt()
    hashedpassword = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashedpassword.decode('utf-8')

## it is going to be used when user will login and will compare the password with the hashed password
def verify_password(hashedPassword: str, password: str) -> bool:
    #did it just for testing 
    # logging.debug(f"Hashed Password: {hashedPassword}")
    # logging.debug(f"Password: {password}")

    if isinstance(hashedPassword, str):
        hashedPassword = hashedPassword.encode('utf-8')

    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashedPassword)
    except ValueError as e:
        # logging.error(f"Error verifying password: {e}")
        return False

## logging will be just used 
## Will call this to generate the jSON web token 

def create_jwt_token(email: EmailStr, username: str):
    header  = {"alg": "HS256", "typ": "JWT"}
    payload = {"email": email, "username": username}
    token = jwt.encode( payload, settings.SECRET_KEY, settings.ALGORITHM) 
    return "Bearer "+token
## this is just for my understanding
# {
    # JSON  = create_jwt_token("dubeyaayush@gmail.com", "Aayush05")
    # d = JSON.split()
    # print(jwt.decode(d[1], settings.SECRET_KEY, settings.ALGORITHM ))
# }
def decoderofJWT(email: EmailStr, username: str, JSONtoken: str):
    onlytoken = JSONtoken.split()
    decoded_token = jwt.decode(onlytoken[1], settings.SECRET_KEY, settings.ALGORITHM )
    if email == decoded_token["email"] and username == decoded_token["username"]:
        print("User grant this access ")
    else:
        print("They will get logged out")

## we are trying example over here 
# decoderofJWT("dubeyaayush333@gmail.com","Aayush05",create_jwt_token("dubeyaayush333@gmail.com", "Aayush05"))


### oAuth additions of the project 
print("Things are working fine")



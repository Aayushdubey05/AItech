import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import session
from fastapi import FastAPI, HTTPException, APIRouter, Depends, requests
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserLogin
from service.login import Login
from db.session import get_db


loginRouter = APIRouter()
@loginRouter.post('/login/')
def logingin(Userexist: UserLogin, db:Session = Depends(get_db)):
    # Userexist.Email = requests.Request()
    # Userexist.Password = requests.Request()
    # loginfeature = Login(db, Userexist)
    login_response = Login(db, Userexist)
    if login_response.get("response model") == "Login Successfull":
        return RedirectResponse(url=f"/profile/{Userexist.Email}", status_code=303)
    else:
        raise HTTPException(status_code=401, detail=login_response["response model"])

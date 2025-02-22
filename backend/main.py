from fastapi import FastAPI, requests, responses, HTTPException, status
from src.core.config  import settings
from src.db.session import engine
from src.db.base import Base
import uvicorn

# class root:
#     def home():
#         data = {"data": "You are on dashboard/home page"}

def create_tables():
    Base.metadata.create_all(bind=engine)

app = FastAPI()

def start_application():
    app = FastAPI(title=settings.ProjectName, version=settings.ProjectVersion)
    create_tables()
    return app

@app.get("/")
def home():
    return {"data": "You are on dashboard/home page"}

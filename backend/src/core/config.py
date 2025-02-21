from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
import os
from pathlib import Path
from dotenv import load_dotenv, dotenv_values

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    ProjectName: str = "autojob"
    ProjectVersion: str = "0.1.0"

    # database info
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB : str = os.getenv("POSTGRES_DB")
    POSTGRES_HOST : str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT")
    DATABASE_URL : str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # database connection

settings = Settings()
print(settings.ProjectName)
print(settings.DATABASE_URL)








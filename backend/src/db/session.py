import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings



SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
        print("Database connected")
    finally:
        print("Database Diconnected")
        db.close()        

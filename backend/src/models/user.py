import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy import Column, Integer, String
from db.base import Base
#defining the model for user signup

# def create_tables():
#     Base.metadata.create_all(bind=engine)

# def start_application():
#     app = FASTAPI(title=settings.ProjectName, version=settings.ProjectVersion)
#     create_tables()
#     return app

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Email = Column(String, unique=True, index=True)
    Password = Column(String)
    Mobile = Column(String)


user = User()
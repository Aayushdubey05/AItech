import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from db.base import Base
#defining the model for user signup
#defining the new model for the resume link storing and path storing 

# def create_tables():
#     Base.metadata.create_all(bind=engine)

# def start_application():
#     app = FASTAPI(title=settings.ProjectName, version=settings.ProjectVersion)
#     create_tables()
#     return app

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)   # Change Name → name
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # Change Password → password
    mobile = Column(String, nullable=False)
    user_profiles = relationship("Profile", backref=backref('user', uselist = False)) #to maintain one-to-one relationship between signup and profile

class Profile(Base):
    __tablename__='user_profiles'
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    name = Column(String,nullable=False)
    email = Column(String,unique=True,index=True, nullable=False)
    city = Column(String,nullable=True)
    states = Column(String,nullable=True)
    country = Column(String, nullable=False) 
    resumeUploaded = Column(Boolean,default=False)
    resume_path = Column(String,default=None,nullable=True)
    resume_link = Column(String,default=None,nullable=True)
    profileimage = Column(Boolean,default=False) 
    linkedin_id = Column(String,nullable=True)
    github_id = Column(String, nullable=True)
    Coding_profiles = Column(String,nullable=True)
    skill_set = Column(String,nullable=True)
    years_of_experience = Column(Integer,nullable=True)
    desired_roles = Column(String,nullable=True)
    users = relationship("User", back_populates="profile") #to maintain one-to-one relationship between signup and profile
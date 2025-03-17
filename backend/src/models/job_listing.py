import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.config import settings, sessionmaker
from db.base import Base
from db.session import SessionLocal, get_db
from sqlalchemy import Column, String, INTEGER, VARCHAR, Integer
class ListedJobs(Base):
    id = Column(Integer, primary_key=True, index=True)
    job_link = Column(String, unique=True, nullable=False)
    job_title = Column(String, nullable=False)
    job_discription = Column(String, nullable=False)
    job_type = Column(String, nullable=False)
    job_location = Column(String, nullable=False)
    job_company = Column(String, nullable=False)
    




import os 
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pydantic import BaseModel
from models.job_listing import ListedJobs
from typing import Optional


class LinkedinJobs(BaseModel):
    JobTitle: str
    CompanyName: str
    JobLocation: str
    JobDescription: Optional[str] = None
    JobType: Optional[str] = None
    JobLink: str

    class Config:
        orm_mode = True

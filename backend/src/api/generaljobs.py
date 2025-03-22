from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import declarative_base, Session
from db.session import get_db
from schemas.jobsfetch import LinkedinJobs
from models.job_listing import ListedJobs


job_fetch_router = APIRouter()

@job_fetch_router.get('/jobs/', response_model = list[LinkedinJobs])
def availjobs(db: Session = Depends(get_db)):
    
    try:
        availjobs = db.query(
            ListedJobs.job_title,
            ListedJobs.job_company,
            ListedJobs.job_location,
            ListedJobs.job_description,
            ListedJobs.job_type,
            ListedJobs.job_link
            ).all()

        

    except Exception as e:
        print(f"Error: {e}")
        return {'details':'An error as occured while fetching the jobs '} 
    
    finally:
        if not availjobs:
            return []
        return [
            {
                "JobTitle": job.job_title,
                "CompanyName": job.job_company,
                "JobLocation": job.job_location,
                "JobDesription": job.job_description,
                "JobType": job.job_type,
                "JobLink": job.job_link
            }
            for job in db.query(ListedJobs).all()
        ]
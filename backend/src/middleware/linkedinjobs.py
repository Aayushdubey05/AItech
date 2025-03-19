import os
import sys 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.config import settings
from models.job_listing import ListedJobs
from scraper.linkedinscraper import run
from fastapi import Depends
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Session, query
from db.session import get_db, SessionLocal

class LoadingOfJobs:
    @staticmethod
    def linkedin_jobs(db: Session):
        linkedin_url = "https://www.linkedin.com/"
        linkedin_jobs = run(linkedin_url)

        existing_jobs_links = {job[0] for job in db.query(ListedJobs.job_link).all()}
        new_jobs = []
        for job in linkedin_jobs:
            if job['link'] not in existing_jobs_links:
                new_jobs.append(
                    ListedJobs(
                        job_link=job['link'],
                        job_title=job['job title'],
                        job_description=job['job description'],
                        job_type=job['job type'],
                        job_location=job['job location'],
                        job_company=job['company name']
                    )
                )
        if new_jobs:
            try:
                db.bulk_save_objects(new_jobs)
                db.commit()
            except Exception as e:
                db.rollback()
                print(f"Error: {e}")
            finally:
                print(f"{len(new_jobs)} new jobs added successfully")
        print("All the jobs added successfully ")

def fetch_the_linkedin():
    db = SessionLocal()
    try:
        LoadingOfJobs.linkedin_jobs(db)
        print("Fetched the jobs in db's ")
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()


fetch_the_linkedin()
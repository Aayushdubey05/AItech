import os 
import sys 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from middleware.linkedinjobs import LoadingOfJobs
from sqlalchemy.orm import Session

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from schemas.resumeschema import ResumeDocuments
from core.config import settings
from db.session import get_db
from models.user import Profile , User 

import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.session import get_db
from models.user import User,Profile
from schemas.user import ProfileSchema

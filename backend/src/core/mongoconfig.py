# import sys #Only for Emergency Case
import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) ## Only for Emergency case 

import pymongo
from dotenv import load_dotenv, dotenv_values
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


# running this just for testing 
MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB = os.getenv("MONGODB")
MONGOCOLLECTION = os.getenv("MONGOCOLLECTION")
class monogoconnection:
    # sourcery skip: inline-immediately-returned-variable

    dbclient = pymongo.MongoClient(MONGODB_URL)
    dbmongo = dbclient[MONGODB]
    mycol = dbmongo[MONGOCOLLECTION]

mongodbconnection = monogoconnection()


import pymongo

async def monogoconnection():
    # sourcery skip: inline-immediately-returned-variable
    
    dbclient = pymongo.MongoClient("mongodb+srv://Admin:Aayu0508@cluster0.e6xave1.mongodb.net/")
    dbmongo = dbclient["user_profile_resume"]
    mycol = dbmongo["resume_docs"]

    return mycol




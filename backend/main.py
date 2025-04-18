from fastapi import FastAPI
from src.core.config import settings
from src.db.session import engine
from src.db.base import Base 
from src.api.create import router as signup_router# ✅ Import signup router
from src.api.login import loginRouter
from src.api.profile import profileRouter
from src.middleware.autorunner import run_scripts
from src.api.generaljobs import job_fetch_router
import uvicorn
import threading
from contextlib import contextmanager, asynccontextmanager 

def create_tables():
    """Create database tables."""
    Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Server is starting {settings.ProjectVersion}")
    # background_thread = threading.Thread(target=run_scripts, daemon=True)
    # background_thread.start()
    # print("Background thread have being started ")
    yield
    print(f"Server goes down {settings.ProjectVersion}")

def start_application():
    """Initialize FastAPI application."""
    app = FastAPI(title=settings.ProjectName, version=settings.ProjectVersion,lifespan=lifespan)
    create_tables()

    # Include all API routers
    app.include_router(signup_router)  # ✅ Added Signuprouter
    app.include_router(loginRouter) # Added LoginRouter
    app.include_router(profileRouter) #Added the ProfileRouter ✅
    app.include_router(job_fetch_router)
    return app

# Initialize the FastAPI app
app = start_application()

@app.get("/")
def home():
    return {"data": "You are on dashboard/home page"}

# Run the app with Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


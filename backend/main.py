from fastapi import FastAPI
from src.core.config import settings
from src.db.session import engine
from src.db.base import Base 
from src.api.create import router as signup_router# ✅ Import signup router
import uvicorn

def create_tables():
    """Create database tables."""
    Base.metadata.create_all(bind=engine)

def start_application():
    """Initialize FastAPI application."""
    app = FastAPI(title=settings.ProjectName, version=settings.ProjectVersion)
    create_tables()

    # Include all API routers
    app.include_router(signup_router)  # ✅ Added router

    return app

# Initialize the FastAPI app
app = start_application()

@app.get("/")
def home():
    return {"data": "You are on dashboard/home page"}

# Run the app with Uvicorn



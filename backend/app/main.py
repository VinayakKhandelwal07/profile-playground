from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from . import models  
from .database import Base, engine
from .routers import health, profile, projects, skills, search

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Profile Playground API")


BASE_DIR = Path(__file__).resolve().parents[2]  # project1/
FRONTEND_DIR = BASE_DIR / "frontend"

# Mount frontend folder as static
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Serve index.html at root
@app.get("/", include_in_schema=False)
async def read_index():
    return FileResponse(FRONTEND_DIR / "index.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(profile.router)
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(search.router)


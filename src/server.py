import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(PROJECT_ROOT, "src", "static")

sys.path.insert(0, PROJECT_ROOT)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Serve static files (project root/src/static)
if os.path.isdir(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Root serves the single-page app index.html when present
@app.get("/")
def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.isfile(index_path):
        return FileResponse(index_path)
    return {"message": "Index not found"}

def get_gemini_service():
    return build("gemini", "v1", developerKey=API_KEY)

# Import router from package
from src.routers.chat import router as chat_router

app.include_router(chat_router, prefix="/api")


if __name__ == "__main__":
    # Run as module path 'src.server:app' if using uvicorn externally
    uvicorn.run("src.server:app", host="0.0.0.0", port=8000, reload=True)

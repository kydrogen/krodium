import os
import sys
from dotenv import load_dotenv

# Load environment variables, and project paths
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(PROJECT_ROOT, "src", "static")
sys.path.insert(0, PROJECT_ROOT)

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
from google.oauth2 import service_account
from googleapiclient.discovery import build
from fastapi.middleware.cors import CORSMiddleware
from routers.chat import router as chat_router

app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# setup routes
app.include_router(chat_router, prefix="/api")

# serve the landing page (index.html)
@app.get("/")
def serve_index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


if __name__ == "__main__":
    uvicorn.run("src.server:app", host="0.0.0.0", port=8000, reload=True)

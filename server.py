import os
from fastapi import FastAPI
import uvicorn
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def get_gemini_service():
    return build("gemini", "v1", developerKey=API_KEY)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(chat_message: ChatMessage):
    return {"response": f"Message received: {chat_message.message}"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)

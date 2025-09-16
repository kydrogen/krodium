from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatMessage(BaseModel):
    message: str


@router.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server (router)!"}


@router.post("/chat")
def chat_endpoint(chat_message: ChatMessage):
    return {"response": f"Message received: {chat_message.message}"}

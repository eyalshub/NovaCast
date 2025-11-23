from fastapi import APIRouter, WebSocket, Depends
from typing import List
from app.api.deps.auth import get_current_user

router = APIRouter()

@router.post("/chat")
async def chat(message: str, user: str = Depends(get_current_user)):
    # Handle chat message processing
    return {"response": f"Received message: {message}"}

@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket, user: str = Depends(get_current_user)):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Process the incoming message and send a response
        await websocket.send_text(f"Message received: {data}")

@router.get("/chat/history", response_model=List[str])
async def get_chat_history(user: str = Depends(get_current_user)):
    # Retrieve chat history for the user
    return ["Chat history item 1", "Chat history item 2"]
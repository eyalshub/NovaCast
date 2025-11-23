from typing import List, Optional
from app.db.models.chat_session import ChatSession
from app.db.connection import get_database

async def create_chat_session(session_data: dict) -> ChatSession:
    db = await get_database()
    chat_session = ChatSession(**session_data)
    await db.chat_sessions.insert_one(chat_session.dict())
    return chat_session

async def get_chat_session(session_id: str) -> Optional[ChatSession]:
    db = await get_database()
    session_data = await db.chat_sessions.find_one({"_id": session_id})
    return ChatSession(**session_data) if session_data else None

async def update_chat_session(session_id: str, update_data: dict) -> Optional[ChatSession]:
    db = await get_database()
    result = await db.chat_sessions.update_one({"_id": session_id}, {"$set": update_data})
    if result.modified_count:
        return await get_chat_session(session_id)
    return None

async def delete_chat_session(session_id: str) -> bool:
    db = await get_database()
    result = await db.chat_sessions.delete_one({"_id": session_id})
    return result.deleted_count > 0

async def list_chat_sessions(limit: int = 10, skip: int = 0) -> List[ChatSession]:
    db = await get_database()
    sessions_data = await db.chat_sessions.find().skip(skip).limit(limit).to_list(length=limit)
    return [ChatSession(**session) for session in sessions_data]
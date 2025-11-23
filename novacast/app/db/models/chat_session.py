from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChatSession(BaseModel):
    id: str
    user_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    messages: list[str]

    class Config:
        orm_mode = True
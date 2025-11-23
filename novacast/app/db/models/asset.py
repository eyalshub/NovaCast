from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Asset(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    url: str
    metadata: Optional[dict] = None

    class Config:
        orm_mode = True
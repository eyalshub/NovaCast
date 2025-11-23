from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Prompt(BaseModel):
    id: Optional[str] = None
    content: str
    version: int
    experiment_flag: Optional[bool] = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
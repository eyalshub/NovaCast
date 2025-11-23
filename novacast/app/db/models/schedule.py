from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Schedule(BaseModel):
    id: Optional[int] = None
    name: str
    start_time: datetime
    end_time: datetime
    recurrence_rule: Optional[str] = None  # e.g., "FREQ=WEEKLY;BYDAY=MO,WE,FR"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
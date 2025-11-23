from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobLog(BaseModel):
    id: Optional[int] = None
    job_name: str
    status: str
    start_time: datetime
    end_time: Optional[datetime] = None
    error_message: Optional[str] = None

    class Config:
        orm_mode = True
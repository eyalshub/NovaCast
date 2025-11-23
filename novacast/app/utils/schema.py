from pydantic import BaseModel, constr, conlist
from typing import List, Optional

class AssetSchema(BaseModel):
    id: int
    name: constr(min_length=1)
    description: Optional[str] = None
    url: constr(regex=r'^(http|https)://')
    created_at: str
    updated_at: str

class ScheduleSchema(BaseModel):
    id: int
    name: constr(min_length=1)
    cron_expression: constr(regex=r'^\S+ \S+ \S+ \S+ \S+$')
    next_run: str
    created_at: str
    updated_at: str

class PromptSchema(BaseModel):
    id: int
    content: constr(min_length=1)
    version: int
    experiment_flag: Optional[bool] = False
    created_at: str
    updated_at: str

class ChatSessionSchema(BaseModel):
    id: int
    user_id: int
    messages: conlist(str, min_items=1)
    created_at: str
    updated_at: str

class JobLogSchema(BaseModel):
    id: int
    job_id: int
    status: constr(regex=r'^(pending|running|completed|failed)$')
    created_at: str
    updated_at: str

# Additional schemas can be defined as needed for other models.
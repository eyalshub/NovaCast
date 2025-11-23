from pydantic import BaseModel, validator
from typing import Any, Dict

class Prompt(BaseModel):
    id: str
    content: str
    version: str
    experiment_flag: bool = False

    @validator('id')
    def id_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('ID must not be empty')
        return v

    @validator('content')
    def content_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Content must not be empty')
        return v

    @validator('version')
    def version_must_be_valid(cls, v):
        if not v.startswith('v'):
            raise ValueError('Version must start with "v"')
        return v

def validate_prompt(prompt: Dict[str, Any]) -> Prompt:
    return Prompt(**prompt)
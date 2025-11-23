from pydantic import BaseModel, Field
from typing import List, Optional

class PromptType(BaseModel):
    id: str = Field(..., description="Unique identifier for the prompt")
    content: str = Field(..., description="The content of the prompt")
    version: str = Field(..., description="Version of the prompt")
    experiment_flag: Optional[bool] = Field(False, description="Flag to indicate if the prompt is part of an experiment")

class PromptSchema(BaseModel):
    prompts: List[PromptType] = Field(..., description="List of prompts")
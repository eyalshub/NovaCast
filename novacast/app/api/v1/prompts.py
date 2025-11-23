from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Prompt(BaseModel):
    id: int
    content: str
    version: str
    experiment_flag: Optional[bool] = False

# In-memory storage for prompts (for demonstration purposes)
prompts_db = []

@router.post("/", response_model=Prompt)
def create_prompt(prompt: Prompt):
    prompts_db.append(prompt)
    return prompt

@router.get("/", response_model=List[Prompt])
def read_prompts():
    return prompts_db

@router.get("/{prompt_id}", response_model=Prompt)
def read_prompt(prompt_id: int):
    for prompt in prompts_db:
        if prompt.id == prompt_id:
            return prompt
    raise HTTPException(status_code=404, detail="Prompt not found")

@router.put("/{prompt_id}", response_model=Prompt)
def update_prompt(prompt_id: int, updated_prompt: Prompt):
    for index, prompt in enumerate(prompts_db):
        if prompt.id == prompt_id:
            prompts_db[index] = updated_prompt
            return updated_prompt
    raise HTTPException(status_code=404, detail="Prompt not found")

@router.delete("/{prompt_id}", response_model=Prompt)
def delete_prompt(prompt_id: int):
    for index, prompt in enumerate(prompts_db):
        if prompt.id == prompt_id:
            return prompts_db.pop(index)
    raise HTTPException(status_code=404, detail="Prompt not found")
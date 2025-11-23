from typing import List, Dict
from app.db.models.prompt import Prompt  # Assuming the Prompt model is defined in models/prompt.py
from app.db.connection import get_database  # Assuming a function to get the database connection

async def create_prompt(prompt_data: Dict) -> Prompt:
    db = await get_database()
    prompt = Prompt(**prompt_data)
    await db.prompts.insert_one(prompt.dict())
    return prompt

async def read_prompt(prompt_id: str) -> Prompt:
    db = await get_database()
    prompt_data = await db.prompts.find_one({"_id": prompt_id})
    return Prompt(**prompt_data) if prompt_data else None

async def update_prompt(prompt_id: str, prompt_data: Dict) -> Prompt:
    db = await get_database()
    await db.prompts.update_one({"_id": prompt_id}, {"$set": prompt_data})
    updated_prompt_data = await db.prompts.find_one({"_id": prompt_id})
    return Prompt(**updated_prompt_data) if updated_prompt_data else None

async def delete_prompt(prompt_id: str) -> bool:
    db = await get_database()
    result = await db.prompts.delete_one({"_id": prompt_id})
    return result.deleted_count > 0

async def list_prompts() -> List[Prompt]:
    db = await get_database()
    prompts_data = await db.prompts.find().to_list(length=None)
    return [Prompt(**data) for data in prompts_data]
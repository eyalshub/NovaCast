from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from app.db.crud.schedules import create_schedule, get_schedule, update_schedule, delete_schedule, get_all_schedules
from app.api.deps.auth import get_current_user

router = APIRouter()

class Schedule(BaseModel):
    id: int
    name: str
    cron_expression: str

@router.post("/", response_model=Schedule)
async def create_new_schedule(schedule: Schedule, current_user: str = Depends(get_current_user)):
    return await create_schedule(schedule)

@router.get("/{schedule_id}", response_model=Schedule)
async def read_schedule(schedule_id: int, current_user: str = Depends(get_current_user)):
    schedule = await get_schedule(schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule

@router.put("/{schedule_id}", response_model=Schedule)
async def update_existing_schedule(schedule_id: int, schedule: Schedule, current_user: str = Depends(get_current_user)):
    updated_schedule = await update_schedule(schedule_id, schedule)
    if not updated_schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return updated_schedule

@router.delete("/{schedule_id}", response_model=dict)
async def delete_existing_schedule(schedule_id: int, current_user: str = Depends(get_current_user)):
    success = await delete_schedule(schedule_id)
    if not success:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {"detail": "Schedule deleted successfully"}

@router.get("/", response_model=List[Schedule])
async def list_schedules(current_user: str = Depends(get_current_user)):
    return await get_all_schedules()
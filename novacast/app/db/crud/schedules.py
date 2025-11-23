from sqlalchemy.orm import Session
from app.db.models.schedule import Schedule
from app.utils.errors import NotFoundError

def create_schedule(db: Session, schedule_data: dict) -> Schedule:
    schedule = Schedule(**schedule_data)
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule

def get_schedule(db: Session, schedule_id: int) -> Schedule:
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise NotFoundError(f"Schedule with id {schedule_id} not found")
    return schedule

def get_schedules(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(Schedule).offset(skip).limit(limit).all()

def update_schedule(db: Session, schedule_id: int, schedule_data: dict) -> Schedule:
    schedule = get_schedule(db, schedule_id)
    for key, value in schedule_data.items():
        setattr(schedule, key, value)
    db.commit()
    db.refresh(schedule)
    return schedule

def delete_schedule(db: Session, schedule_id: int) -> None:
    schedule = get_schedule(db, schedule_id)
    db.delete(schedule)
    db.commit()
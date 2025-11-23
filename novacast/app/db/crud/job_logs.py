from typing import List
from sqlalchemy.orm import Session
from app.db.models.job_log import JobLog

def create_job_log(db: Session, job_log: JobLog) -> JobLog:
    db.add(job_log)
    db.commit()
    db.refresh(job_log)
    return job_log

def get_job_log(db: Session, job_log_id: int) -> JobLog:
    return db.query(JobLog).filter(JobLog.id == job_log_id).first()

def get_job_logs(db: Session, skip: int = 0, limit: int = 100) -> List[JobLog]:
    return db.query(JobLog).offset(skip).limit(limit).all()

def update_job_log(db: Session, job_log_id: int, job_log_data: JobLog) -> JobLog:
    job_log = db.query(JobLog).filter(JobLog.id == job_log_id).first()
    if job_log:
        for key, value in job_log_data.dict().items():
            setattr(job_log, key, value)
        db.commit()
        db.refresh(job_log)
    return job_log

def delete_job_log(db: Session, job_log_id: int) -> bool:
    job_log = db.query(JobLog).filter(JobLog.id == job_log_id).first()
    if job_log:
        db.delete(job_log)
        db.commit()
        return True
    return False
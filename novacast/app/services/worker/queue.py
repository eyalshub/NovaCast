from dramatiq import actor
import time

@actor
def process_job(job_id, data):
    # Simulate job processing
    time.sleep(2)  # Simulate a time-consuming task
    return f"Job {job_id} processed with data: {data}"

def enqueue_job(data):
    job_id = str(time.time())  # Simple job ID based on current time
    process_job.send(job_id, data)
    return job_id

def get_job_status(job_id):
    # Placeholder for job status retrieval logic
    return "Job status is not implemented yet."
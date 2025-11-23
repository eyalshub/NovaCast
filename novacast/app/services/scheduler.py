from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import logging

class Scheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        logging.info("Scheduler started.")

    def add_job(self, func, trigger, **trigger_args):
        self.scheduler.add_job(func, trigger, **trigger_args)
        logging.info(f"Job added: {func.__name__} with trigger {trigger}.")

    def remove_job(self, job_id):
        self.scheduler.remove_job(job_id)
        logging.info(f"Job removed: {job_id}.")

    def start(self):
        self.scheduler.start()
        logging.info("Scheduler started.")

    def shutdown(self):
        self.scheduler.shutdown()
        logging.info("Scheduler shut down.")

    def get_jobs(self):
        return self.scheduler.get_jobs()

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()

    def sample_job():
        logging.info(f"Sample job executed at {datetime.now()}")

    scheduler.add_job(sample_job, CronTrigger(second='*/5'))  # Run every 5 seconds
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
import logging
import json
import os

class CustomJsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'level': record.levelname,
            'message': record.getMessage(),
            'timestamp': self.formatTime(record),
            'trace_id': getattr(record, 'trace_id', None)
        }
        return json.dumps(log_record)

def setup_logging(log_file='logs/app.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(CustomJsonFormatter())

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(CustomJsonFormatter())

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

setup_logging()
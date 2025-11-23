# app/utils/retry.py
from time import sleep
import random

def retry_with_exponential_backoff(func, max_retries=5, base_delay=1, max_delay=60):
    """
    Retries a function with exponential backoff.

    Parameters:
    - func: The function to retry.
    - max_retries: Maximum number of retries.
    - base_delay: Initial delay in seconds.
    - max_delay: Maximum delay in seconds.

    Returns:
    The return value of the function if successful, None otherwise.
    """
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt < max_retries - 1:
                delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
                sleep(delay)
            else:
                raise e  # Re-raise the last exception after max retries

def retry_on_exception(tries=3, exceptions=(Exception,), base_delay=1, max_delay=60):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return retry_with_exponential_backoff(
                lambda: func(*args, **kwargs),
                max_retries=tries,
                base_delay=base_delay,
                max_delay=max_delay
            )
        return wrapper
    return decorator

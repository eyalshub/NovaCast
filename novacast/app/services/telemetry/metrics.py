from prometheus_client import Counter, Histogram

# Metrics for tracking application performance and usage
REQUEST_COUNT = Counter('request_count', 'Total number of requests processed', ['method', 'endpoint'])
RESPONSE_TIME = Histogram('response_time', 'Response time in seconds', ['endpoint'])

def track_request(method: str, endpoint: str):
    """Track the number of requests received."""
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()

def track_response_time(endpoint: str, duration: float):
    """Track the response time for a given endpoint."""
    RESPONSE_TIME.labels(endpoint=endpoint).observe(duration)
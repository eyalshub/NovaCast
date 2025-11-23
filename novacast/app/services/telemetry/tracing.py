from opentelemetry import trace

# Initialize the OpenTelemetry tracer
tracer = trace.get_tracer(__name__)

def start_span(name: str):
    """Start a new span for tracing."""
    return tracer.start_as_current_span(name)

def trace_function(func):
    """Decorator to trace function execution."""
    def wrapper(*args, **kwargs):
        with start_span(func.__name__):
            return func(*args, **kwargs)
    return wrapper

# Example usage of tracing in a function
@trace_function
def example_function(param):
    # Function logic here
    return f"Processed {param}"
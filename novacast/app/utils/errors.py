class CustomError(Exception):
    """Base class for custom exceptions in the application."""
    pass

class NotFoundError(CustomError):
    """Exception raised when a requested resource is not found."""
    def __init__(self, resource: str):
        self.resource = resource
        super().__init__(f"{resource} not found.")

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, message: str):
        super().__init__(f"Validation error: {message}")

class AuthenticationError(CustomError):
    """Exception raised for authentication failures."""
    def __init__(self, message: str = "Authentication failed."):
        super().__init__(message)

class AuthorizationError(CustomError):
    """Exception raised for authorization failures."""
    def __init__(self, message: str = "You do not have permission to perform this action."):
        super().__init__(message)

class InternalServerError(CustomError):
    """Exception raised for internal server errors."""
    def __init__(self, message: str = "An internal server error occurred."):
        super().__init__(message)
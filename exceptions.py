class InvalidInputError(Exception):
    """Exception raised for invalid inputs in the optimizer tool."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class OptimizationError(Exception):
    """Exception raised when optimization fails."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class ConfigurationError(Exception):
    """Exception raised for configuration-related issues."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class ResourceLimitError(Exception):
    """Exception raised when resource limits are exceeded."""
    def __init__(self, limit: str, value: int) -> None:
        message = f'Resource limit exceeded: {limit} with value {value}'
        super().__init__(message)
        self.limit = limit
        self.value = value

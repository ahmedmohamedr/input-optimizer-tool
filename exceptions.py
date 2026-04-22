class InputOptimizerError(Exception):
    """Base class for exceptions in the Input Optimizer module."""
    pass

class InvalidInputError(InputOptimizerError):
    """Exception raised for invalid input errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class OptimizationError(InputOptimizerError):
    """Exception raised when optimization fails."""

    def __init__(self, message: str, code: int) -> None:
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:
        return f'{self.message} (Error code: {self.code})'

class ConfigurationError(InputOptimizerError):
    """Exception raised for configuration issues."""

    def __init__(self, config_key: str, message: str) -> None:
        super().__init__(message)
        self.config_key = config_key
        self.message = message

    def __str__(self) -> str:
        return f'Configuration error with {self.config_key}: {self.message}'

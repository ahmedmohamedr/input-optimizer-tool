class InputOptimizerError(Exception):
    """Base class for exceptions in the input optimizer tool."""
    pass

class ConfigurationError(InputOptimizerError):
    """Exception raised for errors in the configuration."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class ValidationError(InputOptimizerError):
    """Exception raised for validation errors."""
    def __init__(self, message: str, errors: list) -> None:
        super().__init__(message)
        self.errors = errors

    def __str__(self) -> str:
        return f'{super().__str__()}: {self.errors}'

class OptimizationError(InputOptimizerError):
    """Exception raised during optimization process."""
    def __init__(self, message: str, code: int) -> None:
        super().__init__(message)
        self.code = code

    def __str__(self) -> str:
        return f'{super().__str__()} (Error Code: {self.code})'
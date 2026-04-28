class InputOptimizerError(Exception):
    """Custom exception for Input Optimizer errors."""
    pass

class InvalidConfigurationError(InputOptimizerError):
    """Exception raised for invalid configuration errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)

class OptimizationFailedError(InputOptimizerError):
    """Exception raised when optimization fails."""

    def __init__(self, message: str, errors: dict) -> None:
        super().__init__(message)
        self.errors = errors

    def __str__(self) -> str:
        return f'{self.message} | Errors: {self.errors}'

class UnsupportedFileTypeError(InputOptimizerError):
    """Exception raised for unsupported file types."""

    def __init__(self, file_type: str) -> None:
        message = f'Unsupported file type: {file_type}'
        super().__init__(message)

    def __str__(self) -> str:
        return self.message
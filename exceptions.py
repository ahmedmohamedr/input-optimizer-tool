class InputOptimizerError(Exception):
    """Base class for all exceptions raised by the input optimizer."""
    pass

class InvalidInputError(InputOptimizerError):
    """Raised when provided input is invalid."""
    def __init__(self, message):
        super().__init__(message)

class ConfigurationError(InputOptimizerError):
    """Raised for configuration related errors."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f'ConfigurationError: {self.message}'

class ProcessingError(InputOptimizerError):
    """Raised during input processing errors."""
    def __init__(self, message, input_data):
        super().__init__(message)
        self.input_data = input_data

    def __str__(self):
        return f'ProcessingError: {self.message} | Input: {self.input_data}'

# Usage example
# try:
#     raise InvalidInputError('Input cannot be empty')
# except InputOptimizerError as e:
#     print(e)
class InputOptimizerError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidConfigurationError(InputOptimizerError):
    """Exception raised for invalid configuration errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MissingInputError(InputOptimizerError):
    """Exception raised when input is missing."""
    def __init__(self, input_name):
        self.input_name = input_name
        self.message = f"Input '{self.input_name}' is missing."
        super().__init__(self.message)

class OptimizationError(InputOptimizerError):
    """Exception raised for errors during optimization."""
    def __init__(self, details):
        self.details = details
        self.message = f"Optimization failed: {self.details}"
        super().__init__(self.message)

class UnsupportedInputTypeError(InputOptimizerError):
    """Exception raised for unsupported input types."""
    def __init__(self, input_type):
        self.input_type = input_type
        self.message = f"Unsupported input type: {self.input_type}"
        super().__init__(self.message)
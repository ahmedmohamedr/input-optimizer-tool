class InputOptimizerError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidInputError(InputOptimizerError):
    """Raised when input is invalid."""
    def __init__(self, input_value):
        self.input_value = input_value
        self.message = f'Invalid input: {input_value}'
        super().__init__(self.message)

class OptimizationError(InputOptimizerError):
    """Raised when optimization fails."""
    def __init__(self, algorithm, reason):
        self.algorithm = algorithm
        self.reason = reason
        self.message = f'Optimization failed on {algorithm}: {reason}'
        super().__init__(self.message)

class ConfigurationError(InputOptimizerError):
    """Raised when configuration is invalid."""
    def __init__(self, config_file):
        self.config_file = config_file
        self.message = f'Configuration error in: {config_file}'
        super().__init__(self.message)

# Example usage function

def handle_input(value):
    if not isinstance(value, (int, float)):
        raise InvalidInputError(value)
    if value < 0:
        raise OptimizationError('negative_check', 'Input cannot be negative')
    return value * 2
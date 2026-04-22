import re

class InputValidationError(Exception):
    pass

class InputValidator:
    @staticmethod
    def validate_input(user_input):
        if not isinstance(user_input, str):
            raise InputValidationError('Input must be a string.')
        if not user_input.strip():
            raise InputValidationError('Input cannot be empty.')
        if len(user_input) > 50:
            raise InputValidationError('Input exceeds maximum length of 50 characters.')
        if not re.match('^[a-zA-Z0-9_]*$', user_input):
            raise InputValidationError('Input contains invalid characters. Only alphanumeric and underscores are allowed.')
        return True

# Example usage within the main processing loop
if __name__ == '__main__':
    inputs = ['valid_input', 'invalid input!', 'too_long_input_exceeding_fifty_characters_limit']
    for input_str in inputs:
        try:
            InputValidator.validate_input(input_str)
            print(f"'{input_str}' is valid.")
        except InputValidationError as e:
            print(f"Error: {e}")
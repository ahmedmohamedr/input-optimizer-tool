from typing import Any, Dict


class Validator:
    def __init__(self, rules: Dict[str, Any]) -> None:
        """Initializes Validator with specified rules.

        Args:
            rules (Dict[str, Any]): A dictionary containing validation rules for parameters.
        """
        self.rules = rules

    def validate(self, data: Dict[str, Any]) -> bool:
        """Validates the provided data against the rules.

        Args:
            data (Dict[str, Any]): Data to validate.

        Returns:
            bool: True if validation is successful, otherwise False.
        """
        for key, rule in self.rules.items():
            if key not in data:
                print(f'Missing parameter: {key}')
                return False
            if not rule(data[key]):
                print(f'Invalid parameter: {key} with value {data[key]}')
                return False
        return True


# Example usage:
if __name__ == '__main__':
    rules = {
        'username': lambda x: isinstance(x, str) and len(x) > 3,
        'age': lambda x: isinstance(x, int) and 0 < x < 120
    }
    validator = Validator(rules)
    data_to_validate = {'username': 'player1', 'age': 25}
    print(validator.validate(data_to_validate))  # Output: True
    data_to_validate['age'] = 'invalid'
    print(validator.validate(data_to_validate))  # Output: False

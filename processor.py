import json
import re

class InputOptimizer:
    def __init__(self, config):
        self.config = config

    def validate_input(self, input_data):
        if not isinstance(input_data, dict):
            raise ValueError('Input must be a dictionary')
        if 'game_name' not in input_data or not isinstance(input_data['game_name'], str):
            raise ValueError('Game name is required and must be a string')
        if 'sensitivity' in input_data:
            if not (isinstance(input_data['sensitivity'], (int, float)) and 0 <= input_data['sensitivity'] <= 100):
                raise ValueError('Sensitivity must be a number between 0 and 100')
        if 'key_bindings' in input_data:
            if not isinstance(input_data['key_bindings'], dict):
                raise ValueError('Key bindings must be a dictionary')
            for key, value in input_data['key_bindings'].items():
                if not self.is_valid_key_binding(key, value):
                    raise ValueError(f'Invalid key binding: {key} -> {value}')

    def is_valid_key_binding(self, key, value):
        valid_keys = ['W', 'A', 'S', 'D', 'Space', 'Shift']
        valid_key_pattern = re.compile(r'^[A-Z]+$')
        return key in valid_keys and valid_key_pattern.match(value)

    def process_input(self, input_data):
        self.validate_input(input_data)
        # Process the validated input data
        print('Processing input for:', input_data['game_name'])

# Sample usage
if __name__ == '__main__':
    optimizer = InputOptimizer(config={})
    sample_input = {
        'game_name': 'Example Game',
        'sensitivity': 45,
        'key_bindings': {'forward': 'W', 'jump': 'Space'}
    }
    optimizer.process_input(sample_input)
import json
import os

class InputOptimizer:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f'Config file {self.config_file} not found.') 
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise ValueError('Configuration file is not valid JSON.')
    
    def process_input(self, user_input):
        if not isinstance(user_input, str):
            raise TypeError('Input must be a string.')
        elif len(user_input) == 0:
            raise ValueError('Input cannot be an empty string.')
        # Further processing logic goes here, e.g. optimization
        print(f'Processing input: {user_input}')

if __name__ == '__main__':
    optimizer = InputOptimizer('config.json')
    try:
        user_input = 'example input'
        optimizer.process_input(user_input)
    except Exception as e:
        print(f'Error: {e}')
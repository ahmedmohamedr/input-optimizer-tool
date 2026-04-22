import json
from helpers import calculate_metrics
from validators import validate_input

class InputOptimizer:
    def __init__(self, user_input):
        self.user_input = user_input
        self.optimized_input = None

    def optimize(self):
        if validate_input(self.user_input):
            self.optimized_input = self.perform_optimization(self.user_input)
            return self.optimized_input
        raise ValueError('Invalid input data.')

    def perform_optimization(self, input_data):
        return {key: self.optimize_value(value) for key, value in input_data.items()}

    def optimize_value(self, value):
        # Simulating some optimization logic
        return value * 0.9 if isinstance(value, (int, float)) else value

if __name__ == '__main__':
    sample_input = {'graphics': 60, 'sound': 80, 'fps': 30}
    optimizer = InputOptimizer(sample_input)
    optimized_result = optimizer.optimize()
    print(json.dumps(optimized_result, indent=4))
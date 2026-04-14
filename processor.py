import os
import json
import logging

class InputOptimizerProcessor:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)
        self.logger = self.setup_logger()

    def load_config(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Config file not found: {filepath}")
        with open(filepath, 'r') as file:
            return json.load(file)

    def setup_logger(self):
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def process_input(self, input_data):
        self.logger.info('Processing input data...')
        processed = self.optimize_input(input_data)
        self.logger.info('Input data processed successfully')
        return processed

    def optimize_input(self, input_data):
        if not isinstance(input_data, dict):
            self.logger.error('Invalid input: expected a dictionary')
            raise ValueError('Input must be a dictionary')
        return {k: v for k, v in input_data.items() if v is not None}

if __name__ == '__main__':
    processor = InputOptimizerProcessor('config.json')
    sample_input = {'resolution': '1920x1080', 'fullscreen': True, 'volume': None}
    optimized_input = processor.process_input(sample_input)
    print(optimized_input)
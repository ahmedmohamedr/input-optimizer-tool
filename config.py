import json
import os

def load_config(file_path='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    
    if not os.path.exists(file_path):
        print(f'{file_path} not found; using defaults.')
        return defaults
    
    with open(file_path, 'r') as config_file:
        try:
            user_config = json.load(config_file)
        except json.JSONDecodeError:
            print('Error decoding JSON; using defaults.')
            return defaults
    
    combined_config = {**defaults, **user_config}
    return combined_config

# Example usage
if __name__ == '__main__':
    default_settings = {
        'resolution': '1920x1080',
        'volume': 70,
        'difficulty': 'normal'
    }
    config = load_config(defaults=default_settings)
    print(config)
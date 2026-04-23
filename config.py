import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'controls': {
        'move_left': 'A',
        'move_right': 'D',
        'jump': 'SPACE',
        'shoot': 'F'
    }
}

def load_configuration(file_path='config.json'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                user_config = json.load(file)
                return merge_configs(DEFAULT_CONFIG, user_config)
            except json.JSONDecodeError:
                print('Error decoding JSON, using defaults.')  
    return DEFAULT_CONFIG


def merge_configs(defaults, user):
    for key, value in user.items():
        if isinstance(value, dict) and key in defaults:
            defaults[key] = merge_configs(defaults[key], value)
        else:
            defaults[key] = value
    return defaults

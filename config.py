import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 0.75,
    'sensitivity': 1.5,
    'hotkeys': {
        'move_up': 'W',
        'move_down': 'S',
        'move_left': 'A',
        'move_right': 'D',
        'shoot': 'SPACE',
    }
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
            return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

    def update_setting(self, key, value):
        if key in self.config:
            self.config[key] = value
            self.save_config()

# Usage: loader = ConfigLoader() 
# loader.update_setting('volume', 0.85)
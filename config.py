import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)
        self.final_config = self.merge_configs()

    def load_config(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as file:
            return json.load(file)

    def merge_configs(self):
        merged = self.default_config.copy()  # Start with defaults
        merged.update(self.user_config)  # Override with user settings
        return merged

    def get(self, key, default=None):
        return self.final_config.get(key, default)

# Example usage:
# loader = ConfigLoader('default_config.json', 'user_config.json')
# print(loader.get('key_name'))
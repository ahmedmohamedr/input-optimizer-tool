import random
import json

def generate_random_settings(base_settings):
    random_settings = {key: random.choice(value) if isinstance(value, list) else value  
                        for key, value in base_settings.items()}
    return random_settings


def save_settings_to_file(settings, filename):
    with open(filename, 'w') as f:
        json.dump(settings, f, indent=4)
    print(f'Settings saved to {filename}')


def load_settings_from_file(filename):
    with open(filename, 'r') as f:
        settings = json.load(f)
    print(f'Settings loaded from {filename}')
    return settings


def apply_multiple_settings(base_settings, settings_list):
    combined_settings = base_settings.copy()
    for settings in settings_list:
        combined_settings.update(settings)
    return combined_settings


def validate_settings(settings, required_keys):
    missing_keys = [key for key in required_keys if key not in settings]
    if missing_keys:
        raise ValueError(f'Missing settings: {missing_keys}')
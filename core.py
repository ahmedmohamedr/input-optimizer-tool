import random
import json

def generate_random_settings(num_settings=10):
    settings = {}
    for i in range(num_settings):
        key = f'setting_{i}'
        value = random.randint(1, 100)
        settings[key] = value
    return settings

def load_settings_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            settings = json.load(file)
            return settings
    except Exception as e:
        print(f'Error loading settings: {e}')
        return None

def save_settings_to_file(settings, filepath):
    try:
        with open(filepath, 'w') as file:
            json.dump(settings, file, indent=4)
            print('Settings saved successfully.')
    except Exception as e:
        print(f'Error saving settings: {e}')
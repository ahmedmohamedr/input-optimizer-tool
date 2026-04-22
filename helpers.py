import os
import json

class FileError(Exception):
    pass

class ConfigError(Exception):
    pass

def load_json(file_path):
    if not os.path.isfile(file_path):
        raise FileError(f"File not found: {file_path}")
    try:
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    except json.JSONDecodeError:
        raise ConfigError(f"Invalid JSON in {file_path}")
    except Exception as e:
        raise FileError(f"Error loading file: {e}")


def save_json(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except IOError as e:
        raise FileError(f"Unable to write to file: {file_path}, error: {e}")


def validate_config(config):
    required_keys = ['resolution', 'volume', 'controls']
    for key in required_keys:
        if key not in config:
            raise ConfigError(f"Missing key in config: {key}")
    if not isinstance(config['volume'], int) or not (0 <= config['volume'] <= 100):
        raise ConfigError("Volume must be an integer between 0 and 100.")
    return True

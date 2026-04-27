import json
import os
import logging

logging.basicConfig(level=logging.INFO)

def load_config(file_path):
    if not os.path.isfile(file_path):
        logging.error(f"Config file not found: {file_path}")
        raise FileNotFoundError(f"Config file not found: {file_path}")
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
            return config
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        raise ValueError(f"Invalid JSON in config file: {file_path}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise


def validate_config(config):
    required_keys = ['resolution', 'fullscreen', 'volume']
    for key in required_keys:
        if key not in config:
            logging.error(f"Missing required config key: {key}")
            raise KeyError(f"Missing required config key: {key}")
        if not isinstance(config[key], (str, bool, int)):
            logging.error(f"Invalid type for config key '{key}': {type(config[key])}")
            raise TypeError(f"Invalid type for config key '{key}': {type(config[key])}")


def main():
    try:
        config = load_config('config.json')
        validate_config(config)
        logging.info("Configuration loaded and validated successfully!")
    except Exception as e:
        logging.critical(f"Failed to load config: {e}")


if __name__ == '__main__':
    main()
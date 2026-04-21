import json
import os

def load_game_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError('Game data file not found.')
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON format in game data file.')


def save_game_data(file_path, data):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(file_path, new_data):
    current_data = load_game_data(file_path)
    current_data.update(new_data)
    save_game_data(file_path, current_data)


def format_game_data(data):
    formatted = json.dumps(data, indent=4)
    return formatted

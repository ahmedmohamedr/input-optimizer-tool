import json
from datetime import datetime


def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def timestamp_data(data):
    data['timestamp'] = datetime.utcnow().isoformat()
    return data


def filter_character_data(data, min_level=1):
    return [char for char in data['characters'] if char['level'] >= min_level]


def get_high_score(data):
    return max(item['score'] for item in data['scores'])


def format_scoreboard(data):
    return '\n'.join(f"{idx + 1}. {item['player_name']}: {item['score']}" for idx, item in enumerate(sorted(data['scores'], key=lambda x: x['score'], reverse=True)))
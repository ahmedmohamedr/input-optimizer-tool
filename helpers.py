import json
from collections import defaultdict

def load_game_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def save_game_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def optimize_player_stats(data):
    optimized_stats = defaultdict(lambda: {'score': 0, 'wins': 0})
    for player in data['players']:
        optimized_stats[player['name']]['score'] += player['score']
        optimized_stats[player['name']]['wins'] += player['wins']
    return dict(optimized_stats)


def calculate_average_score(data):
    total_score = sum(player['score'] for player in data['players'])
    return total_score / len(data['players']) if data['players'] else 0


def get_top_players(data, top_n=5):
    sorted_players = sorted(data['players'], key=lambda x: x['score'], reverse=True)
    return sorted_players[:top_n]
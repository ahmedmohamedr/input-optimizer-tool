import json
import numpy as np

def load_game_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def normalize_scores(data):
    scores = [entry['score'] for entry in data if 'score' in entry]
    max_score = np.max(scores)
    min_score = np.min(scores)
    for entry in data:
        if 'score' in entry:
            entry['normalized_score'] = (entry['score'] - min_score) / (max_score - min_score) if max_score > min_score else 0
    return data

def filter_high_scores(data, threshold=0.7):
    return [entry for entry in data if entry.get('normalized_score', 0) > threshold]

if __name__ == '__main__':
    file_path = 'game_data.json'
    game_data = load_game_data(file_path)
    normalized_data = normalize_scores(game_data)
    high_scores = filter_high_scores(normalized_data)
    print(high_scores)
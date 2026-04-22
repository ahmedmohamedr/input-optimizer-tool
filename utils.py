import json
import os
from typing import Any, Dict, Union

def load_game_data(file_path: str) -> Union[Dict[str, Any], None]:
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return None

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")
            return None
    return data

def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {file_path}")

def update_game_score(data: Dict[str, Any], new_score: int) -> Dict[str, Any]:
    current_score = data.get('score', 0)
    data['score'] = max(current_score, new_score)
    return data

# Example usage:
# data = load_game_data('game_data.json')
# if data:
#     updated_data = update_game_score(data, 150)
#     save_game_data('game_data.json', updated_data)
import json

class GameData:
    def __init__(self, player_id, score, level):
        self.player_id = player_id
        self.score = score
        self.level = level

    def to_dict(self):
        return {
            'player_id': self.player_id,
            'score': self.score,
            'level': self.level
        }

def save_game_data(file_path, game_data):
    with open(file_path, 'w') as file:
        json_data = [data.to_dict() for data in game_data]
        json.dump(json_data, file, indent=4)

def load_game_data(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        return [GameData(**data) for data in json_data]  

if __name__ == '__main__':
    sample_data = [GameData('player1', 150, 5), GameData('player2', 200, 6)]
    save_game_data('game_data.json', sample_data)
    loaded_data = load_game_data('game_data.json')
    print(loaded_data)
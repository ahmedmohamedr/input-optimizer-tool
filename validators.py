import re

class InputValidator:
    @staticmethod
    def is_valid_username(username):
        return bool(re.match('^[A-Za-z0-9_]{3,15}$', username))

    @staticmethod
    def is_valid_score(score):
        return isinstance(score, int) and 0 <= score <= 100

    @staticmethod
    def is_valid_game_mode(mode):
        valid_modes = ['singleplayer', 'multiplayer', 'co-op']
        return mode in valid_modes

    @staticmethod
    def validate_user_data(user_data):
        if not InputValidator.is_valid_username(user_data.get('username', '')):
            raise ValueError('Invalid username! Must be 3-15 characters long, alphanumeric or underscore.\n')
        if not InputValidator.is_valid_score(user_data.get('score', -1)):
            raise ValueError('Invalid score! Must be an integer between 0 and 100.\n')
        if not InputValidator.is_valid_game_mode(user_data.get('game_mode', '')):
            raise ValueError('Invalid game mode! Must be one of: singleplayer, multiplayer, co-op.\n')
        return True

# Example Usage
if __name__ == '__main__':
    try:
        user_data = {'username': 'Player1', 'score': 95, 'game_mode': 'multiplayer'}
        InputValidator.validate_user_data(user_data)
        print('User data is valid!')
    except ValueError as e:
        print(e)
import re

class GameDataValidator:
    @staticmethod
    def validate_player_name(name):
        if not (1 <= len(name) <= 15):
            raise ValueError("Player name must be between 1 and 15 characters.")
        if not re.match('^[a-zA-Z0-9_]+$', name):
            raise ValueError("Player name can only contain alphanumeric characters and underscores.")
        return True
    
    @staticmethod
    def validate_score(score):
        if not isinstance(score, int) or score < 0:
            raise ValueError("Score must be a non-negative integer.")
        return True
    
    @staticmethod
    def validate_level(level):
        if not (1 <= level <= 100):
            raise ValueError("Level must be between 1 and 100.")
        return True
    
    @staticmethod
    def validate_game_data(player_name, score, level):
        GameDataValidator.validate_player_name(player_name)
        GameDataValidator.validate_score(score)
        GameDataValidator.validate_level(level)
        return True

# Example usage
# validator = GameDataValidator()
# validator.validate_game_data('Player1', 150, 10)  # Should pass
# validator.validate_game_data('Bad Name!', 150, 10)  # Should raise an error
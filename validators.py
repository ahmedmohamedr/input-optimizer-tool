import re

def is_valid_username(username):
    return re.match("^[a-zA-Z0-9_]{3,16}$", username) is not None


def is_valid_password(password):
    return (len(password) >= 8 and 
            any(char.isdigit() for char in password) and 
            any(char.isupper() for char in password) and 
            any(char.islower() for char in password))


def is_valid_email(email):
    regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(regex, email) is not None


def is_valid_game_id(game_id):
    return isinstance(game_id, int) and game_id > 0


if __name__ == '__main__':
    print(is_valid_username('Player1'))  # True
    print(is_valid_password('P@ssw0rd'))  # True
    print(is_valid_email('test@example.com'))  # True
    print(is_valid_game_id(100))  # True

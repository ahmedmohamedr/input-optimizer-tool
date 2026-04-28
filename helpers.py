import json

def validate_user_input(user_input):
    if not isinstance(user_input, dict):
        raise ValueError('Input must be a dictionary')
    required_keys = ['username', 'keybinds']
    for key in required_keys:
        if key not in user_input:
            raise ValueError(f'Missing required key: {key}')
    if not isinstance(user_input['username'], str) or not user_input['username']:
        raise ValueError('Username must be a non-empty string')
    if not isinstance(user_input['keybinds'], dict):
        raise ValueError('Keybinds must be a dictionary')
    return True

def process_input(user_input):
    validate_user_input(user_input)
    # Process the valid input accordingly
    print(json.dumps(user_input, indent=2))

if __name__ == '__main__':
    sample_input = {'username': 'Player1', 'keybinds': {'move_forward': 'W', 'move_back': 'S', 'turn_left': 'A', 'turn_right': 'D'}}
    try:
        process_input(sample_input)
    except ValueError as e:
        print(f'Input error: {e}')
import json
import random

def optimize_input(user_inputs):
    optimized = {key: optimize_value(value) for key, value in user_inputs.items()}
    return json.dumps(optimized)


def optimize_value(value):
    if isinstance(value, list):
        return random.sample(value, min(len(value), 3))
    elif isinstance(value, dict):
        return {k: optimize_value(v) for k, v in value.items()}
    return value


def handle_input(user_inputs):
    try:
        optimized_data = optimize_input(user_inputs)
        print("Optimized Input:", optimized_data)
    except Exception as e:
        print(f"Error processing input: {e}")


if __name__ == '__main__':
    inputs = {
        'settings': ['low', 'medium', 'high'],
        'resolution': {'width': 1920, 'height': 1080},
        'controls': ['keyboard', 'mouse', 'gamepad']
    }
    handle_input(inputs)

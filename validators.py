import json

def is_valid_stats(data):
    required_keys = ['level', 'experience', 'health', 'mana']
    errors = []
    for key in required_keys:
        if key not in data:
            errors.append(f'Missing key: {key}')
        elif not isinstance(data[key], (int, float)):
            errors.append(f'Incorrect type for {key}: expected int/float')
        elif data[key] < 0:
            errors.append(f'Invalid value for {key}: must be non-negative')
    return (len(errors) == 0), errors

def validate_inventory(inventory):
    if not isinstance(inventory, list):
        return False, ['Inventory must be a list']
    for item in inventory:
        if not isinstance(item, dict):
            return False, ['Each inventory item must be a dictionary']
    return True, []

def validate_game_data(data):
    valid_stats, stats_errors = is_valid_stats(data.get('stats', {}))
    valid_inventory, inventory_errors = validate_inventory(data.get('inventory', []))
    errors = stats_errors + inventory_errors
    return (valid_stats and valid_inventory), errors

# Sample usage
if __name__ == '__main__':
    sample_data = json.loads('''{
        "stats": {"level": 5, "experience": 1200, "health": 100, "mana": 50},
        "inventory": [{"item": "Potion", "quantity": 3}, {"item": "Sword", "quantity": 1}]
    }''')
    is_valid, validation_errors = validate_game_data(sample_data)
    print('Is game data valid?', is_valid)
    if not is_valid:
        print('Validation errors:', validation_errors)
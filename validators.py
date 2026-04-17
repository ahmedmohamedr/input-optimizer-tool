import re

class InputValidationError(Exception):
    pass

class InputValidator:
    def __init__(self, valid_commands):
        self.valid_commands = valid_commands
        self.command_pattern = re.compile(r'^[a-zA-Z0-9_]+$')

    def validate_command(self, command):
        if command not in self.valid_commands:
            raise InputValidationError(f'Invalid command: {command}')
        if not self.command_pattern.match(command):
            raise InputValidationError(f'Command contains invalid characters: {command}')
        return True

    def validate_input(self, user_input):
        commands = user_input.split()  
        for command in commands:
            self.validate_command(command)
        return True

if __name__ == '__main__':
    valid_commands = ['move', 'jump', 'shoot']
    validator = InputValidator(valid_commands)
    try:
        validator.validate_input('move jump invalid_command')
    except InputValidationError as e:
        print(e)
    try:
        validator.validate_input('move jump shoot')
        print('All commands are valid!')
    except InputValidationError as e:
        print(e)
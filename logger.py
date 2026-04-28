import logging

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

if __name__ == '__main__':
    log = Logger('GameInputValidator')
    log.info('Logger has been initiated.')
    
    # Example input validation
    inputs = ['valid_input', '', 'another_valid_input', None]
    for i, user_input in enumerate(inputs):
        if not isinstance(user_input, str) or not user_input:
            log.warning(f'Input {i} is invalid: {user_input}')
        else:
            log.info(f'Input {i} is valid: {user_input}')
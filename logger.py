import logging

class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_fmt = "%(asctime)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class Logger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(CustomFormatter())
        self.logger.addHandler(ch)

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

    def exception(self, message):
        self.logger.exception(message)

if __name__ == '__main__':
    logger = Logger('input_optimizer')
    try:
        logger.info('Starting the logger...')
        # Simulate a warning
        x = 5 / 0  # This will raise an exception
    except ZeroDivisionError as e:
        logger.error(f'Error occurred: {e}')
    except Exception as e:
        logger.exception(f'Unexpected error: {e}')
    finally:
        logger.info('Logging session ends.')
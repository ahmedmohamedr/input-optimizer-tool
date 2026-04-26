import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10*1024*1024, backup_count=5):
    logger = logging.getLogger('input_optimizer')
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger

# Example of how to use the logger
if __name__ == '__main__':
    log = setup_logger()
    log.debug('Debugging information')
    log.info('Informational message')
    log.warning('A warning message')
    log.error('An error has occurred')
    log.critical('Critical error, immediate attention needed')
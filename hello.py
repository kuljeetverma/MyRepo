import logging
import os
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

logger_handler = logging.FileHandler('python_logging.log')
logger_handler.setLevel(logging.WARNING)

logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

logger_handler.setFormatter(logger_formatter)

logger.addHandler(logger_handler)


def say_hello(name):
	logger.warning("function called")
	logger.warning("Greetings from {}".format(name))


if __name__ == '__main__':
	say_hello("Kuljeet")

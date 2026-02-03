import logging


# Calling the basicConfig method (without specifying any arguments) 
# creates a StreamHandler object that processes the logs and then
#  displays them in the console.
logging.basicConfig(level=logging.DEBUG, filename='martin_logging.log', filemode='a')

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
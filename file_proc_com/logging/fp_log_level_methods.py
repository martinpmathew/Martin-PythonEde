import logging

logging.basicConfig()
logger = logging.getLogger("Martin")
logger.setLevel(logging.NOTSET)

logger.critical("Your CRITICAL message")
logger.error("Your ERROR message")
logger.warning("Your WARNING message")
logger.info("Your INFO message")
logger.debug("Your DEBUG message")
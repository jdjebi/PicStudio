import logging

logging.basicConfig(format='[%(levelname)s] : %(module)s : %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
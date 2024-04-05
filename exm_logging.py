import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s'
           '%(lineno)s - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.debug('Log of the level DEBUG')


# logging.basicConfig(level=logging.CRITICAL)

# logger = logging.getLogger(__name__)

# logging.debug("This for debug.")
# logging.info("This for info.")
# logging.warning("This is for warning")
# logging.error("This is log of error level")
# logging.critical("This is log of critical lavel")

# print(dir(logger))
"""выводить логи уровня ERROR, но с полным трейсбэком ошибки"""
import logging

logger = logging.getLogger(__name__)

try:
    print(4 / 2)
    print(2 / 0)
except ZeroDivisionError:
    # logger.error('There is exception here.', exc_info=True) # the first option.
    logger.exception('There is an exception here.')  # The second option.

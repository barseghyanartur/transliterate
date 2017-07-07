import logging
import six

from .defaults import LOG_INFO

__title__ = 'transliterate.tests.helpers'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'log_info',
    'py2only',
)

LOGGER = logging.getLogger(__name__)


def log_info(func):
    """Print some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        LOGGER.debug('\n%s', func.__name__)
        LOGGER.debug('============================')
        LOGGER.debug('""" %s """', func.__doc__.strip())
        LOGGER.debug('----------------------------')
        if result is not None:
            try:
                LOGGER.debug(result)
            except Exception:
                LOGGER.debug(result.encode('utf8'))

        return result
    return inner


def py2only(func):
    """Skip the test on Python 3."""
    if not six.PY3:
        return func

    def dummy(self, *args, **kwargs):
        pass

    return dummy

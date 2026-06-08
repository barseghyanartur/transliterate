import logging
from typing import Callable, Concatenate, ParamSpec, TypeVar

from .defaults import LOG_INFO

__title__ = 'transliterate.tests.helpers'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'log_info',
)

LOGGER = logging.getLogger(__name__)


P = ParamSpec('P')
T = TypeVar('T')
R = TypeVar('R')


def log_info(func: Callable[Concatenate[T, P], R]) -> Callable[Concatenate[T, P], None]:
    """Print some useful info."""
    def inner(self: T, *args: P.args, **kwargs: P.kwargs) -> None:
        result = func(self, *args, **kwargs)

        if not LOG_INFO:
            return

        LOGGER.debug('\n%s', func.__name__)
        LOGGER.debug('============================')

        if func.__doc__:
            LOGGER.debug('""" %s """', func.__doc__.strip())

        LOGGER.debug('----------------------------')

        if result is not None:
            LOGGER.debug(result)

    return inner

__title__ = 'transliterate.tests.helpers'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

import six
from six import print_

from transliterate.tests.defaults import PRINT_INFO, TRACK_TIME

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        if TRACK_TIME:
            import simple_timer
            timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop() # Stop timer

        print_('\n{0}'.format(func.__name__))
        print_('============================')
        print_('""" {0} """'.format(func.__doc__.strip()))
        print_('----------------------------')
        if result is not None:
            try:
                print_(result)
            except Exception as e:
                print_(result.encode('utf8'))

        if TRACK_TIME:
            print_('done in {0} seconds'.format(timer.duration))

        return result
    return inner


def py2only(func):
    """
    Skips the test on Python 3.
    """
    if not six.PY3:
        return func

    def dummy(self, *args, **kwargs):
        pass

    return dummy

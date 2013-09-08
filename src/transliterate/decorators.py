__title__ = 'transliterate.decorators'
__version__ = '1.2'
__build__ = 0x000012
__author__ = 'Artur Barseghyan'
__all__ = ('transliterate_function', 'transliterate_method')

import six

from transliterate.utils import translit

class TransliterateFunction(object):
    """
    Function decorator.
    """
    def __init__(self, language_code, reversed=False):
        self.language_code = language_code
        self.reversed = reversed

    def __call__(self, func):
        def inner(*args, **kwargs):
            if six.PY2:
                value = unicode(func(*args, **kwargs))
            else:
                value = func(*args, **kwargs)

            return translit(value, language_code=self.language_code, reversed=self.reversed)
        return inner

transliterate_function = TransliterateFunction


class TransliterateMethod(object):
    """
    Method decorator.
    """
    def __init__(self, language_code, reversed=False):
        self.language_code = language_code
        self.reversed = reversed

    def __call__(self, func):
        def inner(this, *args, **kwargs):
            if six.PY2:
                value = unicode(func(this, *args, **kwargs))
            else:
                value = func(this, *args, **kwargs)

            return translit(value, language_code=self.language_code, reversed=self.reversed)
        return inner

transliterate_method = TransliterateMethod

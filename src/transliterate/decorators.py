__title__ = 'transliterate.decorators'
__version__ = '0.6'
__build__ = 0x000006
__author__ = 'Artur Barseghyan'
__all__ = ('transliterate_function', 'transliterate_method')

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
            value = unicode(func(*args, **kwargs))
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
            value = unicode(func(this, *args, **kwargs))
            return translit(value, language_code=self.language_code, reversed=self.reversed)
        return inner

transliterate_method = TransliterateMethod

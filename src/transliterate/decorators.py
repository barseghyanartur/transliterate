from .utils import translit

__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2023 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'transliterate_function',
    'transliterate_method',
)


class TransliterateFunction(object):
    """Function decorator."""

    def __init__(self, language_code, reversed=False):
        self.language_code = language_code
        self.reversed = reversed

    def __call__(self, func):
        def inner(*args, **kwargs):
            value = func(*args, **kwargs)

            return translit(value,
                            language_code=self.language_code,
                            reversed=self.reversed)
        return inner


transliterate_function = TransliterateFunction


class TransliterateMethod(object):
    """Method decorator."""

    def __init__(self, language_code, reversed=False):
        self.language_code = language_code
        self.reversed = reversed

    def __call__(self, func):
        def inner(this, *args, **kwargs):
            value = func(this, *args, **kwargs)

            return translit(value,
                            language_code=self.language_code,
                            reversed=self.reversed)
        return inner


transliterate_method = TransliterateMethod

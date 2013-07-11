__all__ = ('transliterate_function',)

from transliterate.utils import translit

class TransliterateFunction(object):
    def __init__(self, language_code, reversed=False):
        self.language_code = language_code
        self.reversed = reversed

    def __call__(self, func):
        def inner(*args, **kwargs):
            value = unicode(func(*args, **kwargs))
            return translit(value, language_code=self.language_code, reversed=self.reversed)
        return inner

transliterate_function = TransliterateFunction

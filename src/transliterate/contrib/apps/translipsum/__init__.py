__title__ = 'transliterate.contrib.apps.translipsum.__init__'
__version__ = '1.2'
__build__ = 0x000012
__author__ = 'Artur Barseghyan'
__all__ = ('TranslipsumGenerator',)

from lipsum import Generator

from transliterate.utils import translit

class TranslipsumGenerator(Generator):
    """
    Lorem ipsum generator.
    """
    def __init__(self, language_code, reversed=False, *args, **kwargs):
        self._language_code = language_code
        self._reversed = reversed
        super(TranslipsumGenerator, self).__init__(*args, **kwargs)

    def generate_sentence(self, *args, **kwargs):
        value = super(TranslipsumGenerator, self).generate_sentence(*args, **kwargs)
        return translit(value, language_code=self._language_code, reversed=self._reversed)

    def generate_paragraph(self, *args, **kwargs):
        value = super(TranslipsumGenerator, self).generate_paragraph(*args, **kwargs)
        return translit(value, language_code=self._language_code, reversed=self._reversed)

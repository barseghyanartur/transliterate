# -*- coding: utf-8 -*-

from transliterate import autodiscover
from transliterate.utils import get_available_languages, translit
from transliterate.decorators import transliterate_function

autodiscover()

print '\nOriginal text\n---------------------------------------'
text = "Lorem ipsum dolor sit amet"
print text

print '\nTransliteration to Armenian\n---------------------------------------'
print translit(text, 'hy')

print '\nTransliteration to Russian\n---------------------------------------'
print translit(text, 'ru')

print '\nList of available (registered) languages\n---------------------------------------'
print get_available_languages()

reversed_text = u'Լօրեմ իպսում դoլoր սիտ ամետ'
print '\nReversed transliteration from Armenian\n---------------------------------------'
print translit(reversed_text, 'hy', reversed=True)

reversed_text = u'Лорем ипсум долор сит амет'
print '\nReversed transliteration from Russian\n---------------------------------------'
print translit(reversed_text, 'ru', reversed=True)

print '\nTesting the decorator #1\n---------------------------------------'
@transliterate_function(language_code='hy')
def decorator_test_armenian(text):
    return text

print decorator_test_armenian(u"Lorem ipsum dolor sit amet")

print '\nTesting the decorator #2\n---------------------------------------'
@transliterate_function(language_code='hy', reversed=True)
def decorator_test_armenian_reversed(text):
    return text

print decorator_test_armenian(u"Լօրեմ իպսում դoլoր սիտ ամետ")

print '\nRegistering custom language pack\n---------------------------------------'
from transliterate.base import TranslitLanguagePack, registry

class ExampleLanguagePack(TranslitLanguagePack):
    """
    Example language pack.
    """
    language_code = "example"
    language_name = "Example"
    mapping = (
        u"abcdefghij",
        u"1234567890",
    )

registry.register(ExampleLanguagePack)

print '\nList of available (registered) languages after registering a new language pack \n---------------------------------------'
print get_available_languages()

print '\nTransliteration to Example\n---------------------------------------'
print translit(text, 'example')

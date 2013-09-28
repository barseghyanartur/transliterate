# -*- coding: utf-8 -*-

from transliterate.discover import autodiscover
from transliterate.conf import set_setting
from transliterate import get_available_language_codes, translit

set_setting('DEBUG', True)

# Autodiscover available language packs
#autodiscover()

print '\nOriginal text\n---------------------------------------'
text = "Lorem ipsum dolor sit amet"
print text

print '\nTransliteration to Armenian\n---------------------------------------'
print translit(text, 'hy')

print '\nTransliteration to Russian\n---------------------------------------'
print translit(text, 'ru')

print '\nList of available (registered) languages\n---------------------------------------'
print get_available_language_codes()

print '\nReversed transliteration from Armenian\n---------------------------------------'
print translit(u'Լօրեմ իպսում դoլoր սիտ ամետ', 'hy', reversed=True)

print '\nReversed transliteration from Russian\n---------------------------------------'
print translit(u'Лорем ипсум долор сит амет', 'ru', reversed=True)

print '\nTesting the function decorator\n---------------------------------------'
from transliterate.decorators import transliterate_function

@transliterate_function(language_code='hy')
def decorator_test_armenian(text):
    return text

print decorator_test_armenian(u"Lorem ipsum dolor sit amet")

print '\nTesting the method decorator\n---------------------------------------'
from transliterate.decorators import transliterate_method

class DecoratorTest(object):
    @transliterate_method(language_code='ru')
    def decorator_test_russian(self, text):
        return text

print DecoratorTest().decorator_test_russian(u"Lorem ipsum dolor sit amet")

print '\nTesting the decorator in reversed mode\n---------------------------------------'
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
print get_available_language_codes()

print '\nTransliteration to Example\n---------------------------------------'
print translit(text, 'example')

print '\nTransliterated lorem ipsum generator \n---------------------------------------'
from transliterate.contrib.apps.translipsum import TranslipsumGenerator
g_am = TranslipsumGenerator(language_code='hy')

print 'Generating paragraphs'
print g_am.generate_paragraph()

g_ru = TranslipsumGenerator(language_code='ru')

print '\nGenerating sentenses'
print g_ru.generate_sentence()

print '\nLanguage detection\n---------------------------------------'
from transliterate.utils import detect_language

print detect_language(u'Լօրեմ իպսում դօլօր սիտ ամետ')

print detect_language(u'Лорем ипсум долор сит амет')

print '\nSlugify\n---------------------------------------'
from transliterate.utils import slugify

print slugify(u'Լօրեմ իպսում դօլօր սիտ ամետ')

print slugify(u'Лорем ипсум долор сит амет')

print slugify(u'Lorem ipsum dolor sit amet')

print '\nGeneral testing\n---------------------------------------'
from transliterate.utils import get_available_language_packs

for language_pack in get_available_language_packs():
    print 'Testing language pack %s %s' % (language_pack.language_code, language_pack.language_name)
    print 'Reversed test:'
    for letter in language_pack.mapping[1]:
        print letter, ' --> ', translit(letter, language_pack.language_code, reversed=True)

    print 'Normal test:'
    for letter in language_pack.mapping[0]:
        print letter, ' --> ', translit(letter, language_pack.language_code)

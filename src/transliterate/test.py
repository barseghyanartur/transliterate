# -*- coding: utf-8 -*-

__title__ = 'transliterate.tests'
__version__ = '0.9'
__build__ = 0x000009
__author__ = 'Artur Barseghyan'
__all__ = ('TransliterateTest',)

import unittest

#import simple_timer

from transliterate import autodiscover
from transliterate.conf import set_setting, get_setting, reset_to_defaults_settings
from transliterate import defaults
from transliterate.utils import get_available_language_codes, translit, detect_language, slugify
from transliterate.utils import get_available_language_packs
from transliterate.decorators import transliterate_function, transliterate_method
from transliterate.base import TranslitLanguagePack, registry
from transliterate.contrib.apps.translipsum import TranslipsumGenerator

TRACK_TIME = True

def track_time(func):
    """
    Prints some useful info.
    """
    if not TRACK_TIME:
        return func

    def inner(self, *args, **kwargs):
        #timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        #timer.stop() # Stop timer

        print '\n%s' % func.__name__
        print '============================'
        print '""" %s """' % func.__doc__.strip()
        print '----------------------------'
        if result is not None: print result
        #print 'done in %s seconds' % timer.duration

        return result
    return inner


class TransliterateTest(unittest.TestCase):
    """
    Tests of ``transliterate.utils.translit``.
    """
    def setUp(self):
        self.latin_text = u"Lorem ipsum dolor sit amet"
        self.armenian_text = u'Լօրեմ իպսում դօլօր սիտ ամետ'
        self.cyrillic_text = u'Лорем ипсум долор сит амет'
        self.georgian_text = u'Ⴊორემ იფსუმ დოლორ სით ამეთ'
        self.greek_text = u'Λορεμ ιψθμ δολορ σιτ αμετ'
        #reset_to_defaults_settings()

    @track_time
    def test_01_get_available_language_codes(self):
        """
        Test ``autodiscover`` and ``get_available_language_codes``.
        """
        res = get_available_language_codes()
        res.sort()
        c = ['el', 'hy', 'ka', 'ru']
        c.sort()
        self.assertEqual(res, c)
        return res

    @track_time
    def test_02_translit_latin_to_armenian(self):
        """
        Test transliteration from Latin to Armenian.
        """
        res = translit(self.latin_text, 'hy')
        self.assertEqual(res, self.armenian_text)
        return res

    @track_time
    def test_03_translit_latin_to_georgian(self):
        """
        Test transliteration from Latin to Georgian.
        """
        res = translit(self.latin_text, 'ka')
        self.assertEqual(res, self.georgian_text)
        return res

    @track_time
    def test_04_translit_latin_to_greek(self):
        """
        Test transliteration from Latin to Greek.
        """
        res = translit(self.latin_text, 'el')
        self.assertEqual(res, self.greek_text)
        return res

    @track_time
    def test_05_translit_latin_to_cyrillic(self):
        """
        Test transliteration from Latin to Cyrillic.
        """
        res = translit(self.latin_text, 'ru')
        self.assertEqual(res, self.cyrillic_text)
        return res

    @track_time
    def test_06_translit_armenian_to_latin(self):
        """
        Test transliteration from Armenian to Latin.
        """
        res = translit(self.armenian_text, 'hy', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @track_time
    def test_07_translit_georgian_to_latin(self):
        """
        Test transliteration from Georgian to Latin.
        """
        res = translit(self.georgian_text, 'ka', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @track_time
    def test_08_translit_greek_to_latin(self):
        """
        Test transliteration from Greek to Latin.
        """
        res = translit(self.greek_text, 'el', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @track_time
    def test_09_translit_cyrillic_to_latin(self):
        """
        Test transliteration from Cyrillic to Latun.
        """
        res = translit(self.cyrillic_text, 'ru', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @track_time
    def test_10_function_decorator(self):
        """
        Testing the function decorator from Latin to Armenian.
        """
        @transliterate_function(language_code='hy')
        def decorator_test_armenian(text):
            return text

        res = decorator_test_armenian(self.latin_text)
        self.assertEqual(res, self.armenian_text)

    @track_time
    def test_11_method_decorator(self):
        """
        Testing the method decorator from Latin to Cyrillic.
        """
        class DecoratorTest(object):
            @transliterate_method(language_code='ru')
            def decorator_test_russian(self, text):
                return text

        res = DecoratorTest().decorator_test_russian(self.latin_text)
        self.assertEqual(res, self.cyrillic_text)
        return res

    @track_time
    def test_12_function_decorator(self):
        """
        Testing the function decorator (reversed) from Armenian to Latin.
        """
        @transliterate_function(language_code='hy', reversed=True)
        def decorator_test_armenian_reversed(text):
            return text

        res = decorator_test_armenian_reversed(self.armenian_text)
        self.assertEqual(res, self.latin_text)
        return res

    @track_time
    def test_13_register_custom_language_pack(self):
        """
        Testing registering of a custom language pack.
        """
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

        assert 'example' in get_available_language_codes()
        res = translit(self.latin_text, 'example')
        self.assertEqual(res, 'Lor5m 9psum 4olor s9t 1m5t')
        return res

    @track_time
    def test_14_translipsum_generator_armenian(self):
        """
        Testing the translipsum generator. Generating lorem ipsum paragraphs in Armenian.
        """
        g_am = TranslipsumGenerator(language_code='hy')
        res = g_am.generate_paragraph()
        assert res
        return res

    @track_time
    def test_15_translipsum_generator_georgian(self):
        """
        Testing the translipsum generator. Generating lorem ipsum sentence in Georgian.
        """
        g_ge = TranslipsumGenerator(language_code='ka')
        res = g_ge.generate_sentence()
        assert res
        return res

    @track_time
    def test_16_translipsum_generator_greek(self):
        """
        Testing the translipsum generator. Generating lorem ipsum sentence in Greek.
        """
        g_el = TranslipsumGenerator(language_code='el')
        res = g_el.generate_sentence()
        assert res
        return res

    @track_time
    def test_17_translipsum_generator_cyrillic(self):
        """
        Testing the translipsum generator. Generating lorem ipsum sentence in Cyrillic.
        """
        g_ru = TranslipsumGenerator(language_code='ru')
        res = g_ru.generate_sentence()
        assert res
        return res

    @track_time
    def test_18_language_detection_armenian(self):
        """
        Testing language detection. Detecting Amenian.
        """
        res = detect_language(self.armenian_text)
        self.assertEqual(res, 'hy')
        return res

    @track_time
    def test_19_language_detection_georgian(self):
        """
        Testing language detection. Detecting Georgian.
        """
        res = detect_language(self.georgian_text)
        self.assertEqual(res, 'ka')
        return res

    @track_time
    def test_20_language_detection_greek(self):
        """
        Testing language detection. Detecting Greek.
        """
        #set_setting('DEBUG', True)
        res = detect_language(self.greek_text)
        #reset_to_defaults_settings()
        self.assertEqual(res, 'el')
        return res

    @track_time
    def test_21_language_detection_cyrillic(self):
        """
        Testing language detection. Detecting Russian (Cyrillic).
        """
        res = detect_language(self.cyrillic_text)
        self.assertEqual(res, 'ru')
        return res

    @track_time
    def test_22_slugify_armenian(self):
        """
        Testing slugify from Armenian.
        """
        res = slugify(self.armenian_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @track_time
    def test_23_slugify_georgian(self):
        """
        Testing slugify from Georgian.
        """
        res = slugify(self.georgian_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @track_time
    def test_24_slugify_greek(self):
        """
        Testing slugify from Greek.
        """
        res = slugify(self.greek_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @track_time
    def test_25_slugify_cyrillic(self):
        """
        Testing slugify from Cyrillic.
        """
        res = slugify(self.cyrillic_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @track_time
    def test_26_override_settings(self):
        """
        Testing settings override.
        """
        def override_settings():
            return get_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS')

        self.assertEqual(defaults.LANGUAGE_DETECTION_MAX_NUM_KEYWORDS, override_settings())

        set_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS', 10)
        
        self.assertEqual(10, override_settings())

        return override_settings()

    @track_time
    def __test_27_mappings(self):
        """
        Testing mappings.
        """
        for language_pack in get_available_language_packs():
            print 'Testing language pack %s %s' % (language_pack.language_code, language_pack.language_name)
            print 'Reversed test:'
            for letter in language_pack.mapping[1]:
                print letter, ' --> ', translit(letter, language_pack.language_code, reversed=True)

            print 'Normal test:'
            for letter in language_pack.mapping[0]:
                print letter, ' --> ', translit(letter, language_pack.language_code)


if __name__ == '__main__':
    unittest.main()

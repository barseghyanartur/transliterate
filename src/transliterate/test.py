# -*- coding: utf-8 -*-

__title__ = 'transliterate.tests'
__version__ = '1.2'
__build__ = 0x000012
__author__ = 'Artur Barseghyan'
__all__ = ('TransliterateTest',)

import unittest
import six
from six import print_

from transliterate import autodiscover
from transliterate.conf import set_setting, get_setting, reset_to_defaults_settings
from transliterate import defaults
from transliterate.utils import get_available_language_codes, translit, detect_language, slugify
from transliterate.utils import get_available_language_packs
from transliterate.decorators import transliterate_function, transliterate_method
from transliterate.base import TranslitLanguagePack, registry

if six.PY2:
    from transliterate.contrib.apps.translipsum import TranslipsumGenerator

PRINT_INFO = True
TRACK_TIME = False

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

        print_('\n%s' % func.__name__)
        print_('============================')
        print_('""" %s """' % func.__doc__.strip())
        print_('----------------------------')
        if result is not None:
            try:
                print_(result)
            except Exception as e:
                print_(result.encode('utf8'))

        if TRACK_TIME:
            print_('done in %s seconds' % timer.duration)

        return result
    return inner


def py2only(func):
    """
    Skips the test on Python 3.
    """
    if six.PY2:
        return func

    def dummy(self, *args, **kwargs):
        pass

    return dummy


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
        self.hebrew_text = u'Lורeמ יpסuמ דולור סית אמeת'
        #reset_to_defaults_settings()

    @print_info
    def test_01_get_available_language_codes(self):
        """
        Test ``autodiscover`` and ``get_available_language_codes``.
        """
        res = get_available_language_codes()
        res.sort()
        c = ['el', 'hy', 'ka', 'ru'] #'he', 
        c.sort()
        self.assertEqual(res, c)
        return res

    @print_info
    def test_02_translit_latin_to_armenian(self):
        """
        Test transliteration from Latin to Armenian.
        """
        res = translit(self.latin_text, 'hy')
        self.assertEqual(res, self.armenian_text)
        return res

    @print_info
    def test_03_translit_latin_to_georgian(self):
        """
        Test transliteration from Latin to Georgian.
        """
        res = translit(self.latin_text, 'ka')
        self.assertEqual(res, self.georgian_text)
        return res

    @print_info
    def test_04_translit_latin_to_greek(self):
        """
        Test transliteration from Latin to Greek.
        """
        res = translit(self.latin_text, 'el')
        self.assertEqual(res, self.greek_text)
        return res

    @print_info
    def __test_05_translit_latin_to_hebrew(self):
        """
        Test transliteration from Latin to Hebrew.
        """
        res = translit(self.latin_text, 'he')
        self.assertEqual(res, self.hebrew_text)
        return res

    @print_info
    def test_06_translit_latin_to_cyrillic(self):
        """
        Test transliteration from Latin to Cyrillic.
        """
        res = translit(self.latin_text, 'ru')
        self.assertEqual(res, self.cyrillic_text)
        return res

    @print_info
    def test_07_translit_armenian_to_latin(self):
        """
        Test transliteration from Armenian to Latin.
        """
        res = translit(self.armenian_text, 'hy', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @print_info
    def test_08_translit_georgian_to_latin(self):
        """
        Test transliteration from Georgian to Latin.
        """
        res = translit(self.georgian_text, 'ka', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @print_info
    def test_09_translit_greek_to_latin(self):
        """
        Test transliteration from Greek to Latin.
        """
        res = translit(self.greek_text, 'el', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @print_info
    def __test_10_translit_hebrew_to_latin(self):
        """
        Test transliteration from Hebrew to Latin.
        """
        res = translit(self.hebrew_text, 'he', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @print_info
    def test_11_translit_cyrillic_to_latin(self):
        """
        Test transliteration from Cyrillic to Latun.
        """
        res = translit(self.cyrillic_text, 'ru', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @print_info
    def test_12_function_decorator(self):
        """
        Testing the function decorator from Latin to Armenian.
        """
        @transliterate_function(language_code='hy')
        def decorator_test_armenian(text):
            return text

        res = decorator_test_armenian(self.latin_text)
        self.assertEqual(res, self.armenian_text)

    @print_info
    def test_13_method_decorator(self):
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

    @print_info
    def test_14_function_decorator(self):
        """
        Testing the function decorator (reversed) from Armenian to Latin.
        """
        @transliterate_function(language_code='hy', reversed=True)
        def decorator_test_armenian_reversed(text):
            return text

        res = decorator_test_armenian_reversed(self.armenian_text)
        self.assertEqual(res, self.latin_text)
        return res

    @print_info
    def test_15_register_custom_language_pack(self):
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

    @py2only
    @print_info
    def test_16_translipsum_generator_armenian(self):
        """
        Testing the translipsum generator. Generating lorem ipsum paragraphs in Armenian.
        """
        g_am = TranslipsumGenerator(language_code='hy')
        res = g_am.generate_paragraph()
        assert res
        return res

    @py2only
    @print_info
    def test_17_translipsum_generator_georgian(self):
        """
        Testing the translipsum generator. Generating lorem ipsum sentence in Georgian.
        """
        g_ge = TranslipsumGenerator(language_code='ka')
        res = g_ge.generate_sentence()
        assert res
        return res

    @py2only
    @print_info
    def test_18_translipsum_generator_greek(self):
        """
        Testing the translipsum generator. Generating lorem ipsum sentence in Greek.
        """
        g_el = TranslipsumGenerator(language_code='el')
        res = g_el.generate_sentence()
        assert res
        return res

    @py2only
    @print_info
    def __test_19_translipsum_generator_hebrew(self):
        """
        Testing the translipsum generator. Generating lorem ipsum sentence in Hebrew.
        """
        g_he = TranslipsumGenerator(language_code='he')
        res = g_he.generate_sentence()
        assert res
        return res

    @py2only
    @print_info
    def test_20_translipsum_generator_cyrillic(self):
        """
        Testing the translipsum generator. Generating lorem ipsum sentence in Cyrillic.
        """
        g_ru = TranslipsumGenerator(language_code='ru')
        res = g_ru.generate_sentence()
        assert res
        return res

    @print_info
    def test_21_language_detection_armenian(self):
        """
        Testing language detection. Detecting Amenian.
        """
        res = detect_language(self.armenian_text)
        self.assertEqual(res, 'hy')
        return res

    @print_info
    def test_22_language_detection_georgian(self):
        """
        Testing language detection. Detecting Georgian.
        """
        res = detect_language(self.georgian_text)
        self.assertEqual(res, 'ka')
        return res

    @print_info
    def test_23_language_detection_greek(self):
        """
        Testing language detection. Detecting Greek.
        """
        #set_setting('DEBUG', True)
        res = detect_language(self.greek_text)
        #reset_to_defaults_settings()
        self.assertEqual(res, 'el')
        return res

    @print_info
    def __test_24_language_detection_hebrew(self):
        """
        Testing language detection. Detecting Hebrew.
        """
        res = detect_language(self.hebrew_text)
        self.assertEqual(res, 'he')
        return res

    @print_info
    def test_25_language_detection_cyrillic(self):
        """
        Testing language detection. Detecting Russian (Cyrillic).
        """
        res = detect_language(self.cyrillic_text)
        self.assertEqual(res, 'ru')
        return res

    @print_info
    def test_26_slugify_armenian(self):
        """
        Testing slugify from Armenian.
        """
        res = slugify(self.armenian_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @print_info
    def test_27_slugify_georgian(self):
        """
        Testing slugify from Georgian.
        """
        res = slugify(self.georgian_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @print_info
    def test_28_slugify_greek(self):
        """
        Testing slugify from Greek.
        """
        res = slugify(self.greek_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @print_info
    def __test_29_slugify_hebrew(self):
        """
        Testing slugify from Hebrew.
        """
        res = slugify(self.hebrew_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @print_info
    def test_30_slugify_cyrillic(self):
        """
        Testing slugify from Cyrillic.
        """
        res = slugify(self.cyrillic_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @print_info
    def test_31_override_settings(self):
        """
        Testing settings override.
        """
        def override_settings():
            return get_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS')

        self.assertEqual(defaults.LANGUAGE_DETECTION_MAX_NUM_KEYWORDS, override_settings())

        set_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS', 10)
        
        self.assertEqual(10, override_settings())

        return override_settings()

    @print_info
    def test_32_auto_translit_reversed(self):
        """
        Test automatic reversed translit (from target script to source script) for Armenian, Georgian, Greek,
        Hebrew and Russian (Cyrillic).
        """
        res = []
        texts = [
            self.armenian_text,
            self.georgian_text,
            self.greek_text,
            #self.hebrew_text,
            self.cyrillic_text
        ]

        for text in texts:
            r = translit(text, reversed=True)
            self.assertEqual(r, self.latin_text)
            res.append(r)

        return res

    @print_info
    def test_33_register_unregister(self):
        """
        Testing register/unregister.
        """
        from transliterate.contrib.languages.hy.translit_language_pack import ArmenianLanguagePack

        class A(TranslitLanguagePack):
            language_code = "ru"
            language_name = "Example"
            mapping = (
                u"abcdefghij",
                u"1234567890",
            )
        # Since key `ru` already exists in the registry it can't be replaced (without force-register).
        res = registry.register(A)
        self.assertTrue(not res)

        # Now with force-register it can.
        res = registry.register(A, force=True)
        self.assertTrue(res)

        # Once we have it there and it's forced, we can't register another.
        res = registry.register(A, force=True)
        self.assertTrue(not res)

        # Unregister non-forced language pack.
        res = registry.unregister(ArmenianLanguagePack)
        self.assertTrue(res and not ArmenianLanguagePack.language_code in get_available_language_codes())

        res = registry.unregister(A)
        self.assertTrue(not res and A.language_code in get_available_language_codes())

    @print_info
    def __test_29_mappings(self):
        """
        Testing mappings.
        """
        for language_pack in get_available_language_packs():
            print_('Testing language pack %s %s' % (language_pack.language_code, language_pack.language_name))
            print_('Reversed test:')
            for letter in language_pack.mapping[1]:
                print_(letter, ' --> ', translit(letter, language_pack.language_code, reversed=True))

            print_('Normal test:')
            for letter in language_pack.mapping[0]:
                print_(letter, ' --> ', translit(letter, language_pack.language_code))


if __name__ == '__main__':
    unittest.main()

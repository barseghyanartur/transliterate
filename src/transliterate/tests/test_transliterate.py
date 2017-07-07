# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
import unittest

from .. import (
    defaults,
    detect_language,
    get_available_language_codes,
    get_available_language_packs,
    slugify,
    translit,
)
from ..base import TranslitLanguagePack, registry
from ..conf import (
    get_setting,
    reset_to_defaults_settings,
    set_setting,
)
from ..contrib.apps.translipsum import TranslipsumGenerator
from ..decorators import (
    transliterate_function,
    transliterate_method,
)
from ..discover import autodiscover

from . import data
from .helpers import log_info


__title__ = 'transliterate.tests.test_transliterate'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('TransliterateTest',)


LOGGER = logging.getLogger(__name__)


class TransliterateTest(unittest.TestCase):
    """Test ``transliterate.utils.translit``."""

    def setUp(self):
        """Set up."""
        self.latin_text = data.latin_text
        self.armenian_text = data.armenian_text
        self.cyrillic_text = data.cyrillic_text
        self.ukrainian_cyrillic_text = data.ukrainian_cyrillic_text
        self.bulgarian_cyrillic_text = data.bulgarian_cyrillic_text
        self.georgian_text = data.georgian_text
        self.greek_text = data.greek_text
        self.hebrew_text = data.hebrew_text
        self.mongolian_cyrillic_text = data.mongolian_cyrillic_text
        # reset_to_defaults_settings()

    @log_info
    def test_01_get_available_language_codes(self):
        """Test ``autodiscover`` and ``get_available_language_codes``."""
        res = get_available_language_codes()
        res.sort()
        c = [
            'bg',
            'el',
            'hy',
            'ka',
            'l1',
            'mk',
            'mn',
            'ru',
            'sr',
            'uk',
        ]
        c.sort()
        self.assertEqual(res, c)
        return res

    @log_info
    def test_02_translit_latin_to_armenian(self):
        """Test transliteration from Latin to Armenian."""
        res = translit(self.latin_text, 'hy')
        self.assertEqual(res, self.armenian_text)
        return res

    @log_info
    def test_03_translit_latin_to_georgian(self):
        """Test transliteration from Latin to Georgian."""
        res = translit(self.latin_text, 'ka')
        self.assertEqual(res, self.georgian_text)
        return res

    @log_info
    def test_04_translit_latin_to_greek(self):
        """Test transliteration from Latin to Greek."""
        res = translit(self.latin_text, 'el')
        self.assertEqual(res, self.greek_text)
        return res

    @log_info
    def __test_05_translit_latin_to_hebrew(self):
        """Test transliteration from Latin to Hebrew."""
        res = translit(self.latin_text, 'he')
        self.assertEqual(res, self.hebrew_text)
        return res

    @log_info
    def test_06_translit_latin_to_cyrillic(self):
        """Test transliteration from Latin to Cyrillic."""
        res = translit(self.latin_text, 'ru')
        self.assertEqual(res, self.cyrillic_text)
        return res

    @log_info
    def test_06_translit_latin_to_ukrainian_cyrillic(self):
        """Test transliteration from Latin to Ukrainian Cyrillic."""
        res = translit(self.latin_text, 'uk')
        self.assertEqual(res, self.ukrainian_cyrillic_text)
        return res

    @log_info
    def test_06_translit_latin_to_bulgarian_cyrillic(self):
        """Test transliteration from Latin to Bulgarian Cyrillic."""
        res = translit(self.latin_text, 'bg')
        self.assertEqual(res, self.bulgarian_cyrillic_text)
        return res

    @log_info
    def test_06_translit_latin_to_mongolian_cyrillic(self):
        """Test transliteration from Latin to Mongolian Cyrillic."""
        res = translit(self.latin_text, 'mn')
        self.assertEqual(res, self.mongolian_cyrillic_text)
        return res

    @log_info
    def test_07_translit_armenian_to_latin(self):
        """Test transliteration from Armenian to Latin."""
        res = translit(self.armenian_text, 'hy', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def test_08_translit_georgian_to_latin(self):
        """Test transliteration from Georgian to Latin."""
        res = translit(self.georgian_text, 'ka', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def test_09_translit_greek_to_latin(self):
        """Test transliteration from Greek to Latin."""
        res = translit(self.greek_text, 'el', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def __test_10_translit_hebrew_to_latin(self):
        """Test transliteration from Hebrew to Latin."""
        res = translit(self.hebrew_text, 'he', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def test_11_translit_cyrillic_to_latin(self):
        """Test transliteration from Cyrillic to Latin."""
        res = translit(self.cyrillic_text, 'ru', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def test_11_translit_ukrainian_cyrillic_to_latin(self):
        """Test transliteration from Ukrainian Cyrillic to Latin."""
        res = translit(self.ukrainian_cyrillic_text, 'uk', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def test_11_translit_bulgarian_cyrillic_to_latin(self):
        """Test transliteration from Bulgarian Cyrillic to Latin."""
        res = translit(self.bulgarian_cyrillic_text, 'bg', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def test_11_translit_mongolian_cyrillic_to_latin(self):
        """Test transliteration from Mongolian Cyrillic to Latin."""
        res = translit(self.mongolian_cyrillic_text, 'mn', reversed=True)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def test_12_function_decorator(self):
        """Test the function decorator from Latin to Armenian."""
        @transliterate_function(language_code='hy')
        def decorator_test_armenian(text):
            return text

        res = decorator_test_armenian(self.latin_text)
        self.assertEqual(res, self.armenian_text)

    @log_info
    def test_13_method_decorator(self):
        """Test the method decorator from Latin to Cyrillic."""
        class DecoratorTest(object):
            @transliterate_method(language_code='ru')
            def decorator_test_russian(self, text):
                return text

        res = DecoratorTest().decorator_test_russian(self.latin_text)
        self.assertEqual(res, self.cyrillic_text)
        return res

    @log_info
    def test_14_function_decorator(self):
        """Test the function decorator (reversed) from Armenian to Latin."""
        @transliterate_function(language_code='hy', reversed=True)
        def decorator_test_armenian_reversed(text):
            return text

        res = decorator_test_armenian_reversed(self.armenian_text)
        self.assertEqual(res, self.latin_text)
        return res

    @log_info
    def test_15_register_custom_language_pack(self):
        """Test registering of a custom language pack."""
        class ExampleLanguagePack(TranslitLanguagePack):
            """Example language pack."""

            language_code = "example"
            language_name = "Example"
            mapping = data.test_15_register_custom_language_pack_mapping

        registry.register(ExampleLanguagePack)

        assert 'example' in get_available_language_codes()
        res = translit(self.latin_text, 'example')
        self.assertEqual(res, 'Lor5m 9psum 4olor s9t 1m5t')
        return res

    @log_info
    def test_16_translipsum_generator_armenian(self):
        """Test the translipsum generator.

        Generating lorem ipsum paragraphs in Armenian.
        """
        g_am = TranslipsumGenerator(language_code='hy')
        res = g_am.generate_paragraph()
        assert res
        return res

    @log_info
    def test_17_translipsum_generator_georgian(self):
        """Test the translipsum generator.

        Generating lorem ipsum sentence in Georgian.
        """
        g_ge = TranslipsumGenerator(language_code='ka')
        res = g_ge.generate_sentence()
        assert res
        return res

    @log_info
    def test_18_translipsum_generator_greek(self):
        """Test the translipsum generator

        Generating lorem ipsum sentence in Greek.
        """
        g_el = TranslipsumGenerator(language_code='el')
        res = g_el.generate_sentence()
        assert res
        return res

    @log_info
    def __test_19_translipsum_generator_hebrew(self):
        """Test the translipsum generator.

        Generating lorem ipsum sentence in Hebrew.
        """
        g_he = TranslipsumGenerator(language_code='he')
        res = g_he.generate_sentence()
        assert res
        return res

    @log_info
    def test_20_translipsum_generator_cyrillic(self):
        """Test the translipsum generator.

        Generating lorem ipsum sentence in Cyrillic.
        """
        g_ru = TranslipsumGenerator(language_code='ru')
        res = g_ru.generate_sentence()
        assert res
        return res

    @log_info
    def test_20_translipsum_generator_ukrainian_cyrillic(self):
        """Test the translipsum generator.

        Generating lorem ipsum sentence in Ukrainian Cyrillic.
        """
        g_uk = TranslipsumGenerator(language_code='uk')
        res = g_uk.generate_sentence()
        assert res
        return res

    @log_info
    def test_20_translipsum_generator_bulgarian_cyrillic(self):
        """Test the translipsum generator.

        Generating lorem ipsum sentence in Bulgarian Cyrillic.
        """
        g_bg = TranslipsumGenerator(language_code='bg')
        res = g_bg.generate_sentence()
        assert res
        return res

    @log_info
    def test_20_translipsum_generator_mongolian_cyrillic(self):
        """Test the translipsum generator.

        Generating lorem ipsum sentence in Mongolian Cyrillic.
        """
        g_bg = TranslipsumGenerator(language_code='mn')
        res = g_bg.generate_sentence()
        assert res
        return res

    @log_info
    def test_21_language_detection_armenian(self):
        """Test language detection.

        Detecting Armenian."""
        res = detect_language(self.armenian_text)
        self.assertEqual(res, 'hy')
        return res

    @log_info
    def test_22_language_detection_georgian(self):
        """Test language detection.

        Detecting Georgian.
        """
        res = detect_language(self.georgian_text)
        self.assertEqual(res, 'ka')
        return res

    @log_info
    def test_23_language_detection_greek(self):
        """Test language detection.

        Detecting Greek.
        """
        res = detect_language(self.greek_text)
        self.assertEqual(res, 'el')
        return res

    @log_info
    def __test_24_language_detection_hebrew(self):
        """Test language detection.

        Detecting Hebrew.
        """
        res = detect_language(self.hebrew_text)
        self.assertEqual(res, 'he')
        return res

    @log_info
    def test_25_language_detection_cyrillic(self):
        """Test language detection.

        Detecting Russian (Cyrillic).
        """
        res = detect_language(self.cyrillic_text)
        self.assertEqual(res, 'ru')
        return res

    @log_info
    def test_25_false_language_detection_cyrillic(self):
        """Test language detection.

        Detecting is not Russian (Cyrillic).
        """
        res = detect_language(self.latin_text)
        self.assertNotEqual(res, 'ru')
        return res

    @log_info
    def __test_25_language_detection_ukrainian_cyrillic(self):
        """Testing language detection.

        Detecting Ukrainian (Cyrillic)."""
        res = detect_language(self.ukrainian_cyrillic_text)
        self.assertEqual(res, 'uk')
        return res

    @log_info
    def __test_25_language_detection_bulgarian_cyrillic(self):
        """Test language detection.

        Detecting Bulgarian (Cyrillic)."""
        res = detect_language(self.bulgarian_cyrillic_text)
        self.assertEqual(res, 'bg')
        return res

    @log_info
    def __test_25_language_detection_mongolian_cyrillic(self):
        """Test language detection.

        Detecting Mongolian (Cyrillic).
        """
        res = detect_language(self.mongolian_cyrillic_text)
        self.assertEqual(res, 'mn')
        return res

    @log_info
    def test_26_slugify_armenian(self):
        """Test slugify from Armenian."""
        res = slugify(self.armenian_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @log_info
    def test_27_slugify_georgian(self):
        """Test slugify from Georgian."""
        res = slugify(self.georgian_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @log_info
    def test_28_slugify_greek(self):
        """Test slugify from Greek."""
        res = slugify(self.greek_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @log_info
    def __test_29_slugify_hebrew(self):
        """Test slugify from Hebrew."""
        res = slugify(self.hebrew_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @log_info
    def test_30_slugify_cyrillic(self):
        """Test slugify from Cyrillic."""
        res = slugify(self.cyrillic_text)
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @log_info
    def test_30_slugify_ukrainian_cyrillic(self):
        """Test slugify from Ukrainian Cyrillic."""
        res = slugify(self.ukrainian_cyrillic_text, language_code='uk')
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @log_info
    def test_30_slugify_bulgarian_cyrillic(self):
        """Test slugify from Bulgarian Cyrillic."""
        res = slugify(self.bulgarian_cyrillic_text, language_code='bg')
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @log_info
    def test_30_slugify_mongolian_cyrillic(self):
        """Test slugify from Mongolian Cyrillic."""
        res = slugify(self.mongolian_cyrillic_text, language_code='mn')
        self.assertEqual(res, 'lorem-ipsum-dolor-sit-amet')
        return res

    @log_info
    def test_31_override_settings(self):
        """Testing settings override."""
        def override_settings():
            return get_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS')

        self.assertEqual(defaults.LANGUAGE_DETECTION_MAX_NUM_KEYWORDS,
                         override_settings())

        set_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS', 10)

        self.assertEqual(10, override_settings())

        return override_settings()

    @log_info
    def test_32_auto_translit_reversed(self):
        """Test automatic reversed translit.

        Test automatic reversed translit (from target script to source script)
        for Armenian, Georgian, Greek and Russian (Cyrillic).
        """
        res = []
        texts = [
            self.armenian_text,
            self.georgian_text,
            self.greek_text,
            self.cyrillic_text
        ]

        for text in texts:
            r = translit(text, reversed=True)
            self.assertEqual(r, self.latin_text)
            res.append(r)

        return res

    @log_info
    def test_33_register_unregister(self):
        """Testing register/un-register."""
        from transliterate.contrib.languages.hy.translit_language_pack import (
            ArmenianLanguagePack
        )

        class A(TranslitLanguagePack):
            """Test class."""

            language_code = "ru"
            language_name = "Example"
            mapping = data.test_33_register_unregister_mapping

        # Since key `ru` already exists in the registry it can't be replaced
        # (without force-register).
        res = registry.register(A)
        self.assertTrue(not res)

        # Now with force-register it can.
        res = registry.register(A, force=True)
        self.assertTrue(res)

        # Once we have it there and it's forced, we can't register another.
        res = registry.register(A, force=True)
        self.assertTrue(not res)

        # Un-register non-forced language pack.
        res = registry.unregister(ArmenianLanguagePack)
        self.assertTrue(
            res and ArmenianLanguagePack.language_code
            not in get_available_language_codes()
        )

        res = registry.unregister(A)
        self.assertTrue(
            not res and A.language_code in get_available_language_codes()
        )

    @log_info
    def __test_34_latin_to_latin(self):
        """Test latin to latin."""

        class LatinToLatinLanguagePack(TranslitLanguagePack):
            """
            Custom language pack which gets rid of accented characters in Greek
            but leaves other characters intact.
            """

            language_code = "l2l"
            language_name = "Latin to Latin"
            mapping = data.test_34_latin_to_latin_mapping
            characters = data.test_34_latin_to_latin_characters
            reversed_characters = \
                data.test_34_latin_to_latin_reversed_characters

        res = registry.register(LatinToLatinLanguagePack)
        self.assertTrue(res)

        text = data.test_34_latin_to_latin_text
        pack = LatinToLatinLanguagePack()
        res = pack.translit(text, strict=True, fail_silently=False)

    @log_info
    def __test_29_mappings(self):
        """Test mappings."""
        for language_pack in get_available_language_packs():
            LOGGER.debug(
                'Testing language pack %s %s',
                language_pack.language_code,
                language_pack.language_name
            )
            LOGGER.debug('Reversed test:')
            for letter in language_pack.mapping[1]:
                LOGGER.debug(
                    (
                        letter,
                        ' --> ',
                        translit(
                            letter,
                            language_pack.language_code,
                            reversed=True
                        )
                     )
                )

            LOGGER.debug('Normal test:')
            for letter in language_pack.mapping[0]:
                LOGGER.debug(
                    (
                        letter,
                        ' --> ',
                        translit(letter, language_pack.language_code)
                    )
                )


if __name__ == '__main__':
    unittest.main()

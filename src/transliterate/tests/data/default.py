# -*- coding: utf-8 -*-

latin_text = u"Lorem ipsum dolor sit amet"
armenian_text = u'Լօրեմ իպսում դօլօր սիտ ամետ'
cyrillic_text = u'Лорем ипсум долор сит амет'
ukrainian_cyrillic_text = u'Лорем іпсум долор сіт амет'
bulgarian_cyrillic_text = u'Лорем ипсум долор сит амет'
georgian_text = u'Ⴊორემ იფსუმ დოლორ სით ამეთ'
greek_text = u'Λορεμ ιψυμ δολορ σιτ αμετ'
hebrew_text = u'Lורeמ יpסuמ דולור סית אמeת'
mongolian_cyrillic_text = u'Лорэм ипсүм долор сит амэт'

test_15_register_custom_language_pack_mapping = (
    u"abcdefghij",
    u"1234567890",
)

test_33_register_unregister_mapping = (
    u"abcdefghij",
    u"1234567890",
)

test_34_latin_to_latin_mapping = (
    u"abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW",
    u"zbgdeailxkhnjmpswtrcqv&ofZBGDEAILXKHNJMPSWTRCQOFV",
)

test_34_latin_to_latin_characters = u"abgdezilxkhmjnpsvtrcqw&of" \
                                    u"ABGDEZILXKHMJNPSVTRCQOFW"

test_34_latin_to_latin_reversed_characters = u"abgdezilxkhmjnpsvtrcqw&of" \
                                             u"ABGDEZILXKHMJNPSVTRCQOFW"

test_34_latin_to_latin_text = u"Lorem ipsum dolor sit amet 123453254593485938"

__title__ = 'transliterate.tests.data.default'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

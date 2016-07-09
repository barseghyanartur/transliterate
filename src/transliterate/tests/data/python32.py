# -*- coding: utf-8 -*-

__title__ = 'transliterate.tests.data.python32'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

latin_text = "Lorem ipsum dolor sit amet"
armenian_text = 'Լօրեմ իպսում դօլօր սիտ ամետ'
cyrillic_text = 'Лорем ипсум долор сит амет'
ukrainian_cyrillic_text = 'Лорем іпсум долор сіт амет'
bulgarian_cyrillic_text = 'Лорем ипсум долор сит амет'
georgian_text = 'Ⴊორემ იფსუმ დოლორ სით ამეთ'
greek_text = 'Λορεμ ιψυμ δολορ σιτ αμετ'
hebrew_text = 'Lורeמ יpסuמ דולור סית אמeת'
mongolian_text = u'Лорэм ипсүм долор сит амет'

test_15_register_custom_language_pack_mapping = (
    "abcdefghij",
    "1234567890",
)

test_33_register_unregister_mapping = (
    "abcdefghij",
    "1234567890",
)

test_34_latin_to_latin_mapping = (
    "abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW",
    "zbgdeailxkhnjmpswtrcqv&ofZBGDEAILXKHNJMPSWTRCQOFV",
)

test_34_latin_to_latin_characters = "abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW"

test_34_latin_to_latin_reversed_characters = "abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW"

test_34_latin_to_latin_text = "Lorem ipsum dolor sit amet 123453254593485938"

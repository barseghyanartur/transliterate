__title__ = 'transliterate.tests.data.default'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'


latin_text = "Lorem ipsum dolor sit amet"
armenian_text = 'Լօրեմ իպսում դօլօր սիտ ամետ'
cyrillic_text = 'Лорем ипсум долор сит амет'
ukrainian_cyrillic_text = 'Лорем іпсум долор сіт амет'
bulgarian_cyrillic_text = 'Лорем ипсум долор сит амет'
georgian_text = 'ლორემ იპსუმ დოლორ სით ამეთ'
greek_text = 'Λορεμ ιψυμ δολορ σιτ αμετ'
hebrew_text = 'Lורeמ יpסuמ דולור סית אמeת'
mongolian_cyrillic_text = 'Лорэм ипсүм долор сит амэт'
serbian_cyrillic_text = 'Лорем ипсум долор сит амет'
pangram_serbian_cyrillic_text = 'Фијуче ветар у шибљу, леди пасаже и куће ' \
                                'иза њих и гунђа у оџацима'
pangram_serbian_latin_text = 'Fijuče vetar u šiblju, ledi pasaže i kuće ' \
                             'iza njih i gunđa u odžacima'

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

test_34_latin_to_latin_characters = "abgdezilxkhmjnpsvtrcqw&of" \
                                    "ABGDEZILXKHMJNPSVTRCQOFW"

test_34_latin_to_latin_reversed_characters = "abgdezilxkhmjnpsvtrcqw&of" \
                                             "ABGDEZILXKHMJNPSVTRCQOFW"

test_34_latin_to_latin_text = "Lorem ipsum dolor sit amet 123453254593485938"

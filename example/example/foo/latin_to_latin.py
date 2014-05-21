# -*- coding: utf-8 -*-
"""
Latin to Latin example.
"""

from transliterate import translit
from transliterate.discover import autodiscover
from transliterate.base import TranslitLanguagePack, registry

# First autodicover bundled language packs.
autodiscover()

class LatinToLatinLanguagePack(TranslitLanguagePack):
    """
    Custom language pack which gets rid of accented characters in Greek but leaves other characters intact.
    """
    language_code = "l2l"
    language_name = "Latin to Latin"
    mapping = (
        u"abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW",
        u"zbgdeailxkhnjmpswtrcqv&ofZBGDEAILXKHNJMPSWTRCQOFV",
    )
    characters = u"abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW"
    reversed_characters = u"abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW"


# Register
registry.register(LatinToLatinLanguagePack)

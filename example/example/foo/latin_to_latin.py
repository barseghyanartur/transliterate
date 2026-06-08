"""
Latin to Latin example.
"""

from transliterate.base import TranslitLanguagePack, registry
from transliterate.discover import autodiscover

# First autodicover bundled language packs.
autodiscover()

class LatinToLatinLanguagePack(TranslitLanguagePack):
    """
    Custom language pack which gets rid of accented characters in Greek but leaves other characters intact.
    """
    language_code = "l2l"
    language_name = "Latin to Latin"
    mapping = (
        "abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW",
        "zbgdeailxkhnjmpswtrcqv&ofZBGDEAILXKHNJMPSWTRCQOFV",
    )
    characters = "abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW"
    reversed_characters = "abgdezilxkhmjnpsvtrcqw&ofABGDEZILXKHMJNPSVTRCQOFW"


# Register
registry.register(LatinToLatinLanguagePack)

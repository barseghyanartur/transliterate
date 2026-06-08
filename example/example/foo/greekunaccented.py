"""
This module was kindly provided by Giorgos Georgiadis <georgiad@gmail.com>, who used `transliterate` to
get rid of accented characters in Greek but leave other characters intact.

:example:

>>> from foo.greekunaccented import *
>>> from transliterate import translit
>>> print(translit(u'άέήίϊΐόύϋΰώΆΈΉΊΪΌΎΫΏ', 'el2'))
αεηιιιουυυωΑΕΗΙΙΟΥΥΩ
"""

from transliterate.base import TranslitLanguagePack, registry
from transliterate.discover import autodiscover

# First autodicover bundled language packs.
autodiscover()

class GreekUnaccentedLanguagePack(TranslitLanguagePack):
    """
    Custom language pack which gets rid of accented characters in Greek but leaves other characters intact.
    """
    language_code = "el2"
    language_name = "Greek without accented characters"
    mapping = (
        "άέήίϊΐόύϋΰώΆΈΉΊΪΌΎΫΏ",
        "αεηιιιουυυωΑΕΗΙΙΟΥΥΩ",
    )

# Register
registry.register(GreekUnaccentedLanguagePack)

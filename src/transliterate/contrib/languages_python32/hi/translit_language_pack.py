# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.hi.translit_language_pack'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HindiLanguagePack',)

from transliterate.base import TranslitLanguagePack, registry

class HindiLanguagePack(TranslitLanguagePack):
    """
    Language pack for Hindi language. See http://en.wikipedia.org/wiki/Hindi for details.
    """
    language_code = "hi"
    language_name = "Hindi"
    character_ranges = ((0x0900, 0x097f),) # Fill this in
    mapping = (
        "aeof", #AEOF
        "अइओफ",
        # ae of
    )
    #reversed_specific_mapping = (
    #    "θΘ",
    #    "uU"
    #)
    pre_processor_mapping = {
        "b": "बी",
        "g": "जी",
        "d": "डी",
        "z": "जड़",
        "h": "एच",
        "i": "आई",
        "l": "अल",
        "m": "ऍम",
        "n": "अन",
        "x": "अक्स",
        "k": "के",
        "p": "पी",
        "r": "आर",
        "s": "एस",
        "t": "टी",
        "y": "वाय",
        "w": "डब्लू",
        "u": "यू",
        "c": "सी",
        "j": "जे",
        "q": "क्यू",
        "z": "जड़",
    }
    detectable = True


#registry.register(HindiLanguagePack)

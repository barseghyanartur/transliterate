# -*- coding: utf-8 -*-

from transliterate.base import TranslitLanguagePack, registry

__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2023 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('HindiLanguagePack',)


class HindiLanguagePack(TranslitLanguagePack):
    """Language pack for Hindi language.

    See `http://en.wikipedia.org/wiki/Hindi` for details.
    """
    language_code = "hi"
    language_name = "Hindi"
    character_ranges = ((0x0900, 0x097f),)  # Fill this in
    mapping = (
        u"aeof",  # AEOF
        u"अइओफ",
        # ae of
    )
    # reversed_specific_mapping = (
    #     u"θΘ",
    #     u"uU"
    # )
    pre_processor_mapping = {
        u"b": u"बी",
        u"g": u"जी",
        u"d": u"डी",
        u"z": u"जड़",
        u"h": u"एच",
        u"i": u"आई",
        u"l": u"अल",
        u"m": u"ऍम",
        u"n": u"अन",
        u"x": u"अक्स",
        u"k": u"के",
        u"p": u"पी",
        u"r": u"आर",
        u"s": u"एस",
        u"t": u"टी",
        u"y": u"वाय",
        u"w": u"डब्लू",
        u"u": u"यू",
        u"c": u"सी",
        u"j": u"जे",
        u"q": u"क्यू",
    }
    detectable = True


# registry.register(HindiLanguagePack)

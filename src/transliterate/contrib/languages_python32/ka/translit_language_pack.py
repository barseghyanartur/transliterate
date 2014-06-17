# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.ka.translit_language_pack'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('GeorgianLanguagePack',)

from transliterate.base import TranslitLanguagePack, registry

class GeorgianLanguagePack(TranslitLanguagePack):
    """
    Language pack for Georgian language. See http://en.wikipedia.org/wiki/Georgian_alphabet for details.
    """
    language_code = "ka"
    language_name = "Georgian"
    character_ranges = ((0x10A0, 0x10C5), (0x10D0, 0x10FC), (0x2D00, 0x2D25))
    mapping = (
        "abgdezilkhmjnpsvturqoABGDEZILKHMJNPSVTURQO",
        "აბგდეზილქჰმჯნფსვთურყოႠႡႢႣႤႦႨႪႵჀႫႿႼႴႱႥႧႳႰႷႭ",
    )
    pre_processor_mapping = {
        "k'": "კ",
        "p'": "პ",
        "zh'": "ჟ",
        "t'": "ტ",
        "gh": "ღ",
        "sh": "შ",
        "ch": "ჩ",
        "ts": "ც",
        "dz": "ძ",
        "ts'": "წ",
        "ch'": "ჭ",
        "kh": "ხ",
        "K'": "Ⴉ",
        "P'": "Ⴎ",
        "Zh'": "Ⴏ",
        "T'": "Ⴒ",
        "Gh": "Ⴖ",
        "Sh": "Ⴘ",
        "Ch": "Ⴙ",
        "Ts": "Ⴚ",
        "Dz": "Ⴛ",
        "Ts'": "Ⴜ",
        "Ch'": "Ⴝ",
        "Kh": "Ⴞ",
    }
    detectable = True


registry.register(GeorgianLanguagePack)

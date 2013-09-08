# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.ka.translit_language_pack'
__version__ = '1.2'
__build__ = 0x000012
__author__ = 'Artur Barseghyan'
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
        u"abgdezilkhmjnpsvturqoABGDEZILKHMJNPSVTURQO",
        u"აბგდეზილქჰმჯნფსვთურყოႠႡႢႣႤႦႨႪႵჀႫႿႼႴႱႥႧႳႰႷႭ",
    )
    pre_processor_mapping = {
        u"k'": u"კ",
        u"p'": u"პ",
        u"zh'": u"ჟ",
        u"t'": u"ტ",
        u"gh": u"ღ",
        u"sh": u"შ",
        u"ch": u"ჩ",
        u"ts": u"ც",
        u"dz": u"ძ",
        u"ts'": u"წ",
        u"ch'": u"ჭ",
        u"kh": u"ხ",
        u"K'": u"Ⴉ",
        u"P'": u"Ⴎ",
        u"Zh'": u"Ⴏ",
        u"T'": u"Ⴒ",
        u"Gh": u"Ⴖ",
        u"Sh": u"Ⴘ",
        u"Ch": u"Ⴙ",
        u"Ts": u"Ⴚ",
        u"Dz": u"Ⴛ",
        u"Ts'": u"Ⴜ",
        u"Ch'": u"Ⴝ",
        u"Kh": u"Ⴞ",
    }

registry.register(GeorgianLanguagePack)

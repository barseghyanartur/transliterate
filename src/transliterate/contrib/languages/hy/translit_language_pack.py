# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.hy.translit_language_pack'
__version__ = '1.0'
__build__ = 0x000010
__author__ = 'Artur Barseghyan'
__all__ = ('ArmenianLanguagePack',)

from transliterate.base import TranslitLanguagePack, registry

class ArmenianLanguagePack(TranslitLanguagePack):
    """
    Language pack for Armenian language. See https://en.wikipedia.org/wiki/Armenian_alphabet for details.
    """
    language_code = "hy"
    language_name = "Armenian"
    character_ranges = ((0x0530, 0x058F), (0xFB10, 0xFB1F))
    mapping = (
        u"abgdezilxkhmjnpsvtrcq&ofABGDEZILXKHMJNPSVTRCQOF",
        u"աբգդեզիլխկհմյնպսվտրցքևօֆԱԲԳԴԵԶԻԼԽԿՀՄՅՆՊՍՎՏՐՑՔՕՖ",
    )
    reversed_specific_mapping = (
        u"ռՌ",
        u"rR"
    )
    pre_processor_mapping = {
        u"e'": u"է",
        u"y": u"ը",
        u"th": u"թ",
        u"jh": u"ժ",
        u"ts": u"ծ",
        u"dz": u"ձ",
        u"gh": u"ղ",
        u"tch": u"ճ",
        u"sh": u"շ",
        u"vo": u"ո",
        u"ch": u"չ",
        u"dj": u"ջ",
        u"ph": u"փ",
        u"u": u"ու",
    }

registry.register(ArmenianLanguagePack)

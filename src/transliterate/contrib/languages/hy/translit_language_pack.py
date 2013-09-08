# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.hy.translit_language_pack'
__version__ = '1.2'
__build__ = 0x000012
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
    reversed_specific_pre_processor_mapping = {
        u"ու": u"u",
        u"Ու": u"U"
    }
    pre_processor_mapping = {
        # lowercase
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

        # uppercase
        u"E'": u"Է",
        u"Y": u"Ը",
        u"Th": u"Թ",
        u"Jh": u"Ժ",
        u"Ts": u"Ծ",
        u"Dz": u"Ձ",
        u"Gh": u"Ղ",
        u"Tch": u"Ճ",
        u"Sh": u"Շ",
        u"Vo": u"Ո",
        u"Ch": u"Չ",
        u"Dj": u"Ջ",
        u"Ph": u"Փ",
        u"U": u"Ու"
    }

registry.register(ArmenianLanguagePack)

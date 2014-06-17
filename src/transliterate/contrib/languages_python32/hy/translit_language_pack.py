# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.hy.translit_language_pack'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
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
        "abgdezilxkhmjnpsvtrcq&ofABGDEZILXKHMJNPSVTRCQOF",
        "աբգդեզիլխկհմյնպսվտրցքևօֆԱԲԳԴԵԶԻԼԽԿՀՄՅՆՊՍՎՏՐՑՔՕՖ",
    )
    reversed_specific_mapping = (
        "ռՌ",
        "rR"
    )
    reversed_specific_pre_processor_mapping = {
        "ու": "u",
        "Ու": "U"
    }
    pre_processor_mapping = {
        # lowercase
        "e'": "է",
        "y": "ը",
        "th": "թ",
        "jh": "ժ",
        "ts": "ծ",
        "dz": "ձ",
        "gh": "ղ",
        "tch": "ճ",
        "sh": "շ",
        "vo": "ո",
        "ch": "չ",
        "dj": "ջ",
        "ph": "փ",
        "u": "ու",

        # uppercase
        "E'": "Է",
        "Y": "Ը",
        "Th": "Թ",
        "Jh": "Ժ",
        "Ts": "Ծ",
        "Dz": "Ձ",
        "Gh": "Ղ",
        "Tch": "Ճ",
        "Sh": "Շ",
        "Vo": "Ո",
        "Ch": "Չ",
        "Dj": "Ջ",
        "Ph": "Փ",
        "U": "Ու"
    }
    detectable = True


registry.register(ArmenianLanguagePack)

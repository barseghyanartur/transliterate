# -*- coding: utf-8 -*-

from transliterate.base import TranslitLanguagePack, registry

class ArmenianLanguagePack(TranslitLanguagePack):
    """
    Language pack for Armenian language. See https://en.wikipedia.org/wiki/Armenian_alphabet for details.
    """
    language_code = "hy"
    language_name = "Armenian"
    mapping = (
        u"abgdezilxkhmjnprsvtrcq&ofABGDEZILXKHMJNPRSVTRCQOF",
        u"աբգդեզիլխկհմյնպռսվտրցքևօֆԱԲԳԴԵԶԻԼԽԿՀՄՅՆՊՌՍՎՏՐՑՔՕՖ",
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

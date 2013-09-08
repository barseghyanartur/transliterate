# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.he.translit_language_pack'
__version__ = '1.2'
__build__ = 0x000012
__author__ = 'Artur Barseghyan'
__all__ = ('HebrewLanguagePack',)

from transliterate.base import TranslitLanguagePack, registry

class HebrewLanguagePack(TranslitLanguagePack):
    """
    Language pack for Hebrew language. See http://en.wikipedia.org/wiki/Hebrew_alphabet for details.
    """
    language_code = "he"
    language_name = "Hebrew"
    character_ranges = ((0x0530, 0x058F), (0xFB10, 0xFB1F))
    mapping = (
        u"abgdvzhilmnsfckrt",
        u"אבגדוזחילמנספצקרת",
    )
    reversed_specific_mapping = (
        u"כלמנפ",
        u"klmnp"
    )
    pre_processor_mapping = {
        # lowercase
        u"ha'": u"ה",
        u"tt": u"ט",
        u"ka": u"כ",
        u"aa": u"ע",
        u"sh": u"ש",
        u"fs": u"ף",
        u"cs": u"ץ",
        u"ms": u"ם",
        u"ns": u"ן",
        u"ks": u"ך",
    }

#registry.register(HebrewLanguagePack)

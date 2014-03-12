# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.uk.translit_language_pack'
__author__ = 'Timofey Pchelintsev'
__copyright__ = 'Copyright (c) 2014 Timofey Pchelintsev'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('UkrainianLanguagePack',)

from transliterate.base import TranslitLanguagePack, registry


class UkrainianLanguagePack(TranslitLanguagePack):
    """
    Language pack for Ukrainian language.
    See http://en.wikipedia.org/wiki/Ukrainian_alphabet for details.
    """
    language_code = "uk"
    language_name = "Ukrainian"
    character_ranges = ((0x0400, 0x04FF), (0x0500, 0x052F))
    mapping = (
        u"abvhgdezyijklmnoprstuf'ABVHGDEZYIJKLMNOPRSTUF'",
        u"абвгґдезиійклмнопрстуфьАБВГҐДЕЗИІЙКЛМНОПРСТУФЬ",
    )
    reversed_specific_mapping = (
        u"ьЬ",
        u"''"
    )
    pre_processor_mapping = {
        u"ye": u"є",
        u"zh": u"ж",
        u"yi": u"ї",
        u"kh": u"х",
        u"ts": u"ц",
        u"ch": u"ч",
        u"sh": u"ш",
        u"shch": u"щ",
        u"ju": u"ю",
        u"ja": u"я",
        u"Ye": u"Є",
        u"Zh": u"Ж",
        u"Yi": u"Ї",
        u"Kh": u"Х",
        u"Ts": u"Ц",
        u"Ch": u"Ч",
        u"Sh": u"Ш",
        u"Shch": u"Щ",
        u"Ju": u"Ю",
        u"Ja": u"Я"
    }


registry.register(UkrainianLanguagePack)

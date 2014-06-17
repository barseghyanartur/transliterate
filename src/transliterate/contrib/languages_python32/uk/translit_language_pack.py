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
        "abvhgdezyijklmnoprstuf'ABVHGDEZYIJKLMNOPRSTUF'",
        "абвгґдезиійклмнопрстуфьАБВГҐДЕЗИІЙКЛМНОПРСТУФЬ",
    )
    reversed_specific_mapping = (
        "ьЬ",
        "''"
    )
    pre_processor_mapping = {
        "ye": "є",
        "zh": "ж",
        "yi": "ї",
        "kh": "х",
        "ts": "ц",
        "ch": "ч",
        "sh": "ш",
        "shch": "щ",
        "ju": "ю",
        "ja": "я",
        "Ye": "Є",
        "Zh": "Ж",
        "Yi": "Ї",
        "Kh": "Х",
        "Ts": "Ц",
        "Ch": "Ч",
        "Sh": "Ш",
        "Shch": "Щ",
        "Ju": "Ю",
        "Ja": "Я"
    }


registry.register(UkrainianLanguagePack)

# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.ru.translit_language_pack'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RussianLanguagePack',)

from transliterate.base import TranslitLanguagePack, registry

class RussianLanguagePack(TranslitLanguagePack):
    """
    Language pack for Russian language. See http://en.wikipedia.org/wiki/Russian_alphabet for details.
    """
    language_code = "ru"
    language_name = "Russian"
    character_ranges = ((0x0400, 0x04FF), (0x0500, 0x052F))
    mapping = (
        "abvgdezijklmnoprstufh'y'ABVGDEZIJKLMNOPRSTUFH'Y'",
        "абвгдезийклмнопрстуфхъыьАБВГДЕЗИЙКЛМНОПРСТУФХЪЫЬ",
    )
    reversed_specific_mapping = (
        "ёэЁЭъьЪЬ",
        "eeEE''''"
    )
    pre_processor_mapping = {
        "zh": "ж",
        "ts": "ц",
        "ch": "ч",
        "sh": "ш",
        "sch": "щ",
        "ju": "ю",
        "ja": "я",
        "Zh": "Ж",
        "Ts": "Ц",
        "Ch": "Ч",
        "Sh": "Ш",
        "Sch": "Щ",
        "Ju": "Ю",
        "Ja": "Я"
    }
    detectable = True


registry.register(RussianLanguagePack)

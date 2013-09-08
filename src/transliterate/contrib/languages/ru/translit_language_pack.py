# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.ru.translit_language_pack'
__version__ = '1.2'
__build__ = 0x000012
__author__ = 'Artur Barseghyan'
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
        u"abvgdezijklmnoprstufh'y'ABVGDEZIJKLMNOPRSTUFH'Y'",
        u"абвгдезийклмнопрстуфхъыьАБВГДЕЗИЙКЛМНОПРСТУФХЪЫЬ",
    )
    reversed_specific_mapping = (
        u"ёэЁЭ",
        u"eeEE"
    )
    pre_processor_mapping = {
        u"zh": u"ж",
        u"ts": u"ц",
        u"ch": u"ч",
        u"sh": u"ш",
        u"sch": u"щ",
        u"ju": u"ю",
        u"ja": u"я",
        u"Zh": u"Ж",
        u"Ts": u"Ц",
        u"Ch": u"Ч",
        u"Sch": u"Щ",
        u"Ju": u"Ю",
        u"Ja": u"Я"
    }

registry.register(RussianLanguagePack)

# -*- coding: utf-8 -*-

from transliterate.base import TranslitLanguagePack, registry

class RussianLanguagePack(TranslitLanguagePack):
    """
    Language pack for Russian language. See http://en.wikipedia.org/wiki/Russian_alphabet for details.
    """
    language_code = "ru"
    language_name = "Russian"
    mapping = (
        u"abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E",
        u"абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
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

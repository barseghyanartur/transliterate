# -*- coding: utf-8 -*-

mapping = (
    u"abvgdjziklmnouprstuufheABVGDJZIKLMNOUPRSTUUFHE",
    u"абвгджзиклмноөпрстуүфхэАБВГДЖЗИКЛМНОӨПРСТУҮФХЭ",
)
reversed_specific_mapping = (
    u"ъьЪЬйЙ",
    u"iiIIiI"
)
pre_processor_mapping = {
    u"ii": u"ы",
    u"II": u"Ы",
    u"ye": u"е",
    u"YE": u"Е",
    u"yo": u"ё",
    u"YO": u"Ё",
    u"ts": u"ц",
    u"TS": u"Ц",
    u"ch": u"ч",
    u"CH": u"Ч",
    u"sh": u"ш",
    u"SH": u"Ш",
    u"sh": u"щ",
    u"SH": u"Щ",
    u"yu": u"ю",
    u"YU": u"Ю",
    u"ya": u"я",
    u"YA": u"Я",
}

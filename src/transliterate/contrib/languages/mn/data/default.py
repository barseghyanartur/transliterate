mapping = (
    "abvgdjziklmnoprstuufhewABVGDJZIKLMNOPRSTUUFHEW",
    "абвгджзиклмнопрстуүфхэвАБВГДЖЗИКЛМНОПРСТУҮФХЭВ",
)
reversed_specific_mapping = (
    "ъьЪЬйЙөӨуУүҮ",
    "iiIIiIoOuUuU"
)
pre_processor_mapping = {
    "ii": "ы",
    "II": "Ы",
    "ye": "е",
    "YE": "Е",
    "yo": "ё",
    "Yo": "Ё",
    "YO": "Ё",
    "ts": "ц",
    "TS": "Ц",
    "ch": "ч",
    "CH": "Ч",
    "sh": "ш",
    "SH": "Ш",
    "yu": "ю",
    "Yu": "Юу",
    "YU": "Ю",
    "ya": "я",
    "YA": "Я",
    "ai": "ай",
    "Ai": "Ай",
    "AI": "АЙ",
    "ei": "эй",
    "Ei": "Эй",
    "EI": "ЭЙ",
    # TODO: There are two values for both "ii" and "II" in the map (see the beginning). Figure out which should remain.
    "ii": "ий",  # noqa: F601
    "Ii": "Ий",
    "II": "ИЙ",  # noqa: F601
    "oi": "ой",
    "Oi": "Ой",
    "OI": "ОЙ",
    "ui": "уй",
    "Ui": "Уй",
    "UI": "УЙ",
    "KH": "Х",
    "kh": "х"
}
reversed_specific_pre_processor_mapping = {
    "щ": "sh",
    "Щ": "SH",
    "ю": "yu",
    "Ю": "Yu",
    "Ч": "Ch",
    "x": "h"
}

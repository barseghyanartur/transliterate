mapping = (
    "abvgdeziyklmnoprstufhABVGDEZIYKLMNOPRSTUFH",
    "абвгдезийклмнопрстуфхАБВГДЕЗИЙКЛМНОПРСТУФХ",
)

reversed_specific_mapping = (
    "ьъЪ",
    "yaA"
)

pre_processor_mapping = {
    "zh": "ж",
    "ts": "ц",
    "ch": "ч",
    "sh": "ш",
    "sht": "щ",
    "yu": "ю",
    "ya": "я",
    "Zh": "Ж",
    "Ts": "Ц",
    "Ch": "Ч",
    "Sh": "Ш",
    "Sht": "Щ",
    "Yu": "Ю",
    "Ya": "Я",
    "Q": "Я", # Bulgarians typers often use "Q" for "Я". Example: KNQZ => КНЯЗ
    "q": "Я", # Bulgarians typers often use "q" for "я". Example: pepelqshka => пепеляшка
}

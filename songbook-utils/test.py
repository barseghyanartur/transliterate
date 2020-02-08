from transliterate.discover import autodiscover
from transliterate import translit, get_available_language_codes
autodiscover()

text = "Лемковино, краю рідний"

print(get_available_language_codes())

print(translit(text, 'lem', reversed=True))
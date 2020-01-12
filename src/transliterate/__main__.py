from transliterate.discover import autodiscover
from transliterate import translit, get_available_language_codes

if __name__ == '__main__':
    autodiscover()
    print(get_available_language_codes())
    text = 'Лемковино, краю рідний'
    print(translit(text, 'lem', reversed=True))
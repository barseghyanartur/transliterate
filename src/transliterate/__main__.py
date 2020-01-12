from transliterate.discover import autodiscover
from transliterate import translit, get_available_language_codes
from functools import partial
import os

autodiscover()

_to_latin = partial(translit, language_code='lem', reversed=True)
_file_path = os.path.join('/', 'home', 'petro', 'dev', 'priv', 'lem-spiwnyk', 'spysany', 'boze_boze_jakij_to_zal.tex')

if __name__ == '__main__':
    text = 'Лемковино, краю рідний'
    with open(_file_path, 'r') as f:
        content = f.read()
        print(_to_latin(content))
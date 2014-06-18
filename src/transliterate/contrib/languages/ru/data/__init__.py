from transliterate.helpers import PY32

if PY32:
    from transliterate.contrib.languages.ru.data.python32 import *
else:
    from transliterate.contrib.languages.ru.data.standard import *

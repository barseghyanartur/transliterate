from transliterate.helpers import PY32

if PY32:
    from transliterate.contrib.languages.uk.data.python32 import *
else:
    from transliterate.contrib.languages.uk.data.standard import *

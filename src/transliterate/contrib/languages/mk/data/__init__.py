from transliterate.helpers import PY32

if PY32:
    from .python32 import *
else:
    from .standard import *

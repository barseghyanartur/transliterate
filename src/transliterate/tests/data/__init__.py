__title__ = 'transliterate.tests.data'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from transliterate.helpers import PY32

if PY32:
    from transliterate.tests.data.python32 import *
else:
    from transliterate.tests.data.normal import *

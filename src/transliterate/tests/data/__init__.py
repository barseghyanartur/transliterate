from transliterate.helpers import PY32

if PY32:
    from transliterate.tests.data.python32 import *
else:
    from transliterate.tests.data.normal import *

__title__ = 'transliterate.tests.data'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

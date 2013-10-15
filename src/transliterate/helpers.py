__title__ = 'transliterate.helpers'
__version__ = '1.5'
__build__ = 0x00000F
__author__ = 'Artur Barseghyan'
__all__ = ('PROJECT_DIR', 'PY2', 'PY3')

import os
import sys

PROJECT_DIR = lambda base: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        (os.path.join(*base) if isinstance(base, (list, tuple)) else base)
    ).replace('\\','/')
)

#PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))

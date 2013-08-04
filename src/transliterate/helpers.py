__title__ = 'transliterate.helpers'
__version__ = '1.0'
__build__ = 0x000010
__author__ = 'Artur Barseghyan'
__all__ = ('PROJECT_DIR',)

import os

PROJECT_DIR = lambda base: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        (os.path.join(*base) if isinstance(base, (list, tuple)) else base)
    ).replace('\\','/')
)

#PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))
from .utils import (
    detect_language,
    get_available_language_codes,
    get_available_language_packs,
    slugify,
    translit
)

__title__ = 'transliterate'
__version__ = '1.9'
__build__ = 0x00001b
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'translit',
    'get_available_language_codes',
    'detect_language',
    'slugify',
    'get_available_language_packs',
)

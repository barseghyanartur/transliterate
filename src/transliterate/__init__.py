__title__ = 'transliterate'
__version__ = '1.7.3'
__build__ = 0x000015
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('translit', 'get_available_language_codes', 'detect_language', 'slugify', 'get_available_language_packs')

from transliterate.utils import translit, get_available_language_codes, detect_language, slugify
from transliterate.utils import get_available_language_packs

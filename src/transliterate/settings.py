__title__ = 'transliterate.settings'
__version__ = '0.7'
__build__ = 0x000007
__author__ = 'Artur Barseghyan'
__all__ = ('LANGUAGES_DIR', 'CONTRIB_DIR', 'LANGUAGE_PACK_MODULE_NAME', 'LANGUAGE_DETECTION_MAX_NUM_KEYWORDS', 'DEBUG')

from transliterate.conf import get_setting

LANGUAGES_DIR = get_setting('LANGUAGES_DIR')
CONTRIB_DIR =  get_setting('CONTRIB_DIR')
LANGUAGE_PACK_MODULE_NAME = get_setting('LANGUAGE_PACK_MODULE_NAME')
LANGUAGE_DETECTION_MAX_NUM_KEYWORDS = get_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS')

DEBUG = get_setting('DEBUG')

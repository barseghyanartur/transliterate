__title__ = 'transliterate.discover'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('autodiscover',)

import os

from six import print_

try:
    from importlib import import_module
except ImportError:
    import_module = __import__

from transliterate.helpers import PROJECT_DIR
from transliterate.conf import get_setting

def autodiscover():
    """
    Auto-discovers the language packs in contrib/apps.
    """
    LANGUAGES_DIR = get_setting('LANGUAGES_DIR')
    LANGUAGE_PACK_MODULE_NAME = get_setting('LANGUAGE_PACK_MODULE_NAME')
    DEBUG = get_setting('DEBUG')

    for app_path in os.listdir(PROJECT_DIR(LANGUAGES_DIR)):
        full_app_path = list(LANGUAGES_DIR)
        full_app_path.append(app_path)
        if os.path.isdir(PROJECT_DIR(full_app_path)):
            try:
                import_module(
                    "transliterate.{0}.{1}.{2}".format(
                        '.'.join(LANGUAGES_DIR),
                        app_path,
                        LANGUAGE_PACK_MODULE_NAME
                    )
                )
            except ImportError as e:
                if DEBUG:
                    print_(e)
            except Exception as e:
                if DEBUG:
                    print_(e)
        else:
            pass

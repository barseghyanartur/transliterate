import os

from six import print_

try:
    from importlib import import_module
except ImportError:
    import_module = __import__

from .conf import get_setting
from .helpers import PROJECT_DIR

__title__ = 'transliterate.discover'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('autodiscover',)


def autodiscover():
    """Auto-discover the language packs in contrib/apps."""
    languages_dir = get_setting('LANGUAGES_DIR')
    language_pack_module_name = get_setting('LANGUAGE_PACK_MODULE_NAME')
    debug = get_setting('DEBUG')

    for app_path in os.listdir(PROJECT_DIR(languages_dir)):
        full_app_path = list(languages_dir)
        full_app_path.append(app_path)
        if os.path.isdir(PROJECT_DIR(full_app_path)):
            try:
                import_module(
                    "transliterate.{0}.{1}.{2}".format(
                        '.'.join(languages_dir),
                        app_path,
                        language_pack_module_name
                    )
                )
            except ImportError as err:
                if debug:
                    print_(err)
            except Exception as err:
                if debug:
                    print_(err)
        else:
            pass

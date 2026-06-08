import os
from importlib import import_module

from .conf import get_setting
from .helpers import PROJECT_DIR

__title__ = 'transliterate.discover'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('autodiscover',)


def autodiscover() -> None:
    """Auto-discover the language packs in contrib/apps."""
    languages_dir: str | None = get_setting('LANGUAGES_DIR')
    language_pack_module_name: str | None = get_setting('LANGUAGE_PACK_MODULE_NAME')

    if languages_dir is None or language_pack_module_name is None:
        return

    debug: bool | None = get_setting('DEBUG')

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
                    print(err)
            except Exception as err:
                if debug:
                    print(err)
        else:
            pass

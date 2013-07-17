import os

try:
    from importlib import import_module
except ImportError:
    import_module = __import__

from transliterate.helpers import PROJECT_DIR
from transliterate.settings import LANGUAGES_DIR, LANGUAGE_PACK_MODULE_NAME

def autodiscover():
    """
    Autodiscovers the language packs in contrib/apps.
    """
    for app_path in os.listdir(PROJECT_DIR(LANGUAGES_DIR)):
        full_app_path = list(LANGUAGES_DIR)
        full_app_path.append(app_path)
        if os.path.isdir(PROJECT_DIR(full_app_path)):
            try:
                import_module(
                    "transliterate.%s.%s.%s" % ('.'.join(LANGUAGES_DIR), app_path, LANGUAGE_PACK_MODULE_NAME)
                    )
            except ImportError, e:
                pass
            except Exception, e:
                pass
        else:
            pass

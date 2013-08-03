__title__ = 'transliterate.conf'
__version__ = '0.7'
__build__ = 0x000007
__author__ = 'Artur Barseghyan'
__all__ = ('get_setting', 'set_setting', 'settings',)

from transliterate import defaults

class Settings(object):
    """
    Settings registry.
    """
    def __init__(self):
        self._settings = {}

    def set(self, name, value):
        """
        Override default settings.

        :param str name:
        :param mixed value:
        """
        self._settings[name] = value

    def get(self, name, default=None):
        """
        Gets a variable from local settings.

        :param str name:
        :param mixed default: Default value.
        :return mixed:
        """
        if self._settings.has_key(name):
            return self._settings.get(name, default)
        elif hasattr(defaults, name):
            return getattr(defaults, name, default)
        else:
            return default

settings = Settings()

get_setting = settings.get

set_setting = settings.set

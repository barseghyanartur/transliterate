__title__ = 'transliterate.conf'
__version__ = '1.2'
__build__ = 0x000012
__author__ = 'Artur Barseghyan'
__all__ = ('get_setting', 'set_setting', 'settings', 'reset_to_defaults_settings')

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
        if name in self._settings:
            return self._settings.get(name, default)
        elif hasattr(defaults, name):
            return getattr(defaults, name, default)
        else:
            return default

    def reset_to_defaults(self):
        """
        Resets settings to defaults.
        """
        self._settings = {}

settings = Settings()

get_setting = settings.get

set_setting = settings.set

reset_to_defaults_settings = settings.reset_to_defaults

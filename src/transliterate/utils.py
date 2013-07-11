__all__ = ('translit', 'get_available_languages')

from transliterate.base import registry

def translit(value, language_code, reversed=False):
    """
    Transliterates the text for the language given.

    :param str value:
    :param str language_code:
    :param bool reversed: If set to True, reversed translation is made.
    :return str:
    """
    cls = registry.get(language_code)
    language_pack = cls()
    return language_pack.translit(value, reversed=reversed)

def get_available_languages():
    """
    Gets list of registered languages.

    :return list:
    """
    return registry._registry.keys()

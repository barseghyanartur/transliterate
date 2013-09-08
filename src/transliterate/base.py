# -*- coding: utf-8 -*-

__title__ = 'transliterate.base'
__version__ = '1.2'
__build__ = 0x000012
__author__ = 'Artur Barseghyan'
__all__ = ('TranslitLanguagePack', 'registry')

import unicodedata
import six

from transliterate.exceptions import ImproperlyConfigured, InvalidRegistryItemType

class TranslitLanguagePack(object):
    """
    Base language pack. The attributes below shall be defined in every language pack.

    ``language_code``: Language code (obligatory). Example value: 'hy', 'ru'.
    ``language_name``: Language name (obligatory). Example value: 'Armenian', 'Russian'.
    ``character_ranges``: Character ranges that are specific to the language. When making a pack, take a look at
        (http://en.wikipedia.org/wiki/List_of_Unicode_characters) for the ranges.
    ``mapping``: Mapping  (obligatory). A tuple, consisting of two strings (source and target). Example value:
        (u'abc', u'աբց').
    ``reversed_specific_mapping``: Specific mapping (one direction only) used when transliterating from target script
        to source script (reversed transliteration).
    ՝՝pre_processor_mapping՝՝: Pre processor mapping (optional). A dictionary mapping for letters that can't be
        represented by a single latin letter.

    :example:
>>>    class ArmenianLanguagePack(TranslitLanguagePack):
>>>    language_code = "hy"
>>>    language_name = "Armenian"
>>>    character_ranges = ((0x0530, 0x058F), (0xFB10, 0xFB1F))
>>>    mapping = (
>>>        u"abgdezilxkhmjnpsvtrcq&ofABGDEZILXKHMJNPSVTRCQOF", # Source script
>>>        u"աբգդեզիլխկհմյնպսվտրցքևօֆԱԲԳԴԵԶԻԼԽԿՀՄՅՆՊՍՎՏՐՑՔՕՖ", # Target script
>>>    )
>>>    reversed_specific_mapping = (
>>>        u"ռՌ",
>>>        u"rR"
>>>    )
>>>    pre_processor_mapping = {
>>>        u"e'": u"է",
>>>        u"y": u"ը",
>>>        u"th": u"թ",
>>>        u"jh": u"ժ",
>>>        u"ts": u"ծ",
>>>        u"dz": u"ձ",
>>>        u"gh": u"ղ",
>>>        u"tch": u"ճ",
>>>        u"sh": u"շ",
>>>        u"vo": u"ո",
>>>        u"ch": u"չ",
>>>        u"dj": u"ջ",
>>>        u"ph": u"փ",
>>>        u"u": u"ու",
>>>    }

    Note, thatn in Python 3 you won't be using u prefix before the strings.
    """
    language_code = None
    language_name = None
    character_ranges = None
    mapping = None
    reversed_specific_mapping = None
    reversed_pre_processor_mapping_keys = []
    reversed_specific_pre_processor_mapping = None
    reversed_specific_pre_processor_mapping_keys = []
    pre_processor_mapping = None
    pre_processor_mapping_keys = []

    def __init__(self):
        try:
            assert self.language_code is not None
            assert self.language_name is not None
            assert self.mapping
        except Exception as e:
            raise ImproperlyConfigured("You should define ``language_code``, ``language_name`` and ``mapping`` "
                                       "properties in your subclassed ``TranslitLanguagePack`` class.")
        super(TranslitLanguagePack, self).__init__()

        # Creating a translation table from the mapping set.
        self.translation_table = {}
        [self.translation_table.update({ord(a): ord(b)}) for a, b in zip(*self.mapping)]

        # Creating a reversed translation table.
        self.reversed_translation_table = dict(zip(self.translation_table.values(), self.translation_table.keys()))

        # If any pre-processor rules defined, reversing them for later use.
        if self.pre_processor_mapping:
            self.reversed_pre_processor_mapping = dict(
                zip(self.pre_processor_mapping.values(), self.pre_processor_mapping.keys())
                )
            self.pre_processor_mapping_keys = self.pre_processor_mapping.keys()
            self.reversed_pre_processor_mapping_keys = self.pre_processor_mapping.values()

        else:
            self.reversed_pre_processor_mapping = None

        if self.reversed_specific_mapping:
            self.reversed_specific_translation_table = {}
            [self.reversed_specific_translation_table.update({ord(a): ord(b)}) \
             for a, b in zip(*self.reversed_specific_mapping)]

        if self.reversed_specific_pre_processor_mapping:
            self.reversed_specific_pre_processor_mapping_keys = self.reversed_specific_pre_processor_mapping.keys()

    def translit(self, value, reversed=False):
        """
        Transliterates the given value according to the rules set in the transliteration pack.

        :param str value:
        :param bool reversed:
        :return str:
        """
        if six.PY2:
            value = unicode(value)

        if reversed:
            # Handling reversed specific translations (one side only).
            if self.reversed_specific_mapping:
                value = value.translate(self.reversed_specific_translation_table)

            if self.reversed_specific_pre_processor_mapping:
                for rule in self.reversed_specific_pre_processor_mapping_keys:
                    value = value.replace(rule, self.reversed_specific_pre_processor_mapping[rule])

            # Handling pre-processor mappings.
            if self.reversed_pre_processor_mapping:
                for rule in self.reversed_pre_processor_mapping_keys:
                    value = value.replace(rule, self.reversed_pre_processor_mapping[rule])

            return value.translate(self.reversed_translation_table)

        if self.pre_processor_mapping:
            for rule in self.pre_processor_mapping_keys:
                value = value.replace(rule, self.pre_processor_mapping[rule])
        return value.translate(self.translation_table)

    @classmethod
    def contains(cls, character):
        """
        Checks if given character belongs to the language pack.

        :return bool:
        """
        if cls.character_ranges:
            char_num = unicodedata.normalize('NFC', character)
            char_num = hex(ord(char_num))
            for character_range in cls.character_ranges:
                range_lower = hex(character_range[0])
                range_upper = hex(character_range[1])
                if char_num >= range_lower and char_num <= range_upper:
                    return True
        return False


class TranslitRegistry(object):
    """
    Language pack registry.
    """
    def __init__(self):
        self._registry = {}
        self._forced = []

    def register(self, cls, force=False):
        """
        Registers the language pack in the registry.

        :param transliterate.base.LanguagePack cls: Subclass of ``transliterate.base.LanguagePack``.
        :param bool force: If set to True, item stays forced. It's not possible to unregister a forced item.
        :return bool: True if registered and False otherwise.
        """
        if not issubclass(cls, TranslitLanguagePack):
            raise InvalidRegistryItemType("Invalid item type `%s` for registry `%s`" % (cls, self.__class__))

        # If item has not been forced yet, add/replace its' value in the registry
        if force:

            if not cls.language_code in self._forced:
                self._registry[cls.language_code] = cls
                self._forced.append(cls.language_code)
                return True
            else:
                return False

        else:

            if cls.language_code in self._registry:
                return False
            else:
                self._registry[cls.language_code] = cls
                return True

    def unregister(self, cls):
        """
        Unregisters an item from registry.

        :param transliterate.base.LanguagePack cls: Subclass of ``transliterate.base.LanguagePack``.
        :return bool: True if unregistered and False otherwise.
        """
        if not issubclass(cls, TranslitLanguagePack):
            raise InvalidRegistryItemType("Invalid item type `%s` for registry `%s`" % (cls, self.__class__))

        # Only non-forced items are allowed to be unregistered.
        if cls.language_code in self._registry and not cls.language_code in self._forced:
            self._registry.pop(cls.language_code)
            return True
        else:
            return False

    def get(self, language_code, default=None):
        """
        Gets the given language pack from the registry.

        :param str language_code:
        :return transliterate.base.LanguagePack: Subclass of ``transliterate.base.LanguagePack``.
        """
        return self._registry.get(language_code, default)


# Register languages by calling registry.register()
registry = TranslitRegistry()

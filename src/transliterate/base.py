__all__ = ('TranslitLanguagePack', 'registry')


class TranslitLanguagePack(object):
    """
    Base language pack. The attributes below shall be defined in every language pack.

    ``language_code``: Language code (obligatory). Example value: 'hy', 'ru'.
    ``language_name``: Language name (obligatory). Example value: 'Armenian', 'Russian'.
    ``mapping``: Mapping  (obligatory). A tuple, consisting of two strings. Example value: (u'abc', u'աբց')
    ՝՝pre_processor_mapping՝՝: Pre processor mapping (optional). A dictionary mapping for letters that can't be
        represented by a single latin letter.

    :example:
>>>    class ArmenianLanguagePack(TranslitLanguagePack):
>>>    language_code = "hy"
>>>    language_name = "Armenian"
>>>    mapping = (
>>>        u"abgdezilxkhmjnprsvtrcq&ofABGDEZILXKHMJNPRSVTRCQOF",
>>>        u"աբգդեզիլխկհմյնպռսվտրցքևօֆԱԲԳԴԵԶԻԼԽԿՀՄՅՆՊՌՍՎՏՐՑՔՕՖ",
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
    """
    language_code = None
    language_name = None
    mapping = None
    pre_processor_mapping = None

    def __init__(self):
        try:
            assert self.language_code is not None
            assert self.language_name is not None
            assert self.mapping
        except Exception, e:
            raise Exception("You should define ``language_code``, ``language_name`` and ``mapping`` properties in "
                            "your subclassed ``TranslitLanguagePack`` class.")
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
        else:
            self.reversed_pre_processor_mapping = None

    def translit(self, value, reversed=False):
        """
        Transliterates the given value according to the rules set in the transliteration pack.

        :param str value:
        :param bool reversed:
        :return str:
        """
        value = unicode(value)
        if reversed:
            if self.reversed_pre_processor_mapping:
                for rule in self.reversed_pre_processor_mapping.keys():
                    value = value.replace(rule, self.reversed_pre_processor_mapping[rule])
            return value.translate(self.reversed_translation_table)

        if self.pre_processor_mapping:
            for rule in self.pre_processor_mapping.keys():
                value = value.replace(rule, self.pre_processor_mapping[rule])
        return value.translate(self.translation_table)


class TranslitRegistry(object):
    """
    Language pack registry.
    """
    def __init__(self):
        self._registry = {}

    def register(self, cls):
        """
        Registers the language pack in the registry.
        :param str language_code:
        :param str path:
        """
        self._registry[cls.language_code] = cls

    def get(self, language_code):
        """
        Gets the given language pack from the registry.

        :param str language_code:
        :return transliterate.base.LanguagePack: Subclass of ``transliterate.base.LanguagePack``.
        """
        if self._registry.has_key(language_code):
            return self._registry[language_code]


# Register languages by calling registry.register()
registry = TranslitRegistry()

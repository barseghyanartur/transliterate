# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.el.translit_language_pack'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('GreekLanguagePack',)

from transliterate.base import TranslitLanguagePack, registry

class GreekLanguagePack(TranslitLanguagePack):
    """
    Language pack for Greek language. See http://en.wikipedia.org/wiki/Greek_alphabet for details.
    """
    language_code = "el"
    language_name = "Greek"
    character_ranges = ((0x0370, 0x03FF), (0x1F00, 0x1FFF))
    mapping = (
        "abgdezhiklmnxoprstyfwuABGDEZHIKLMNXOPRSTYFWU",
        "αβγδεζηικλμνξοπρστυφωθΑΒΓΔΕΖΗΙΚΛΜΝΞΟΠΡΣΤΥΦΩΘ",
    )
    reversed_specific_mapping = (
        "θΘ",
        "uU"
    )
    pre_processor_mapping = {
        "th": "θ",
        "ch": "χ",
        "ps": "ψ",
        "TH": "Θ",
        "CH": "Χ",
        "PS": "Ψ",
    }
    detectable = True


registry.register(GreekLanguagePack)

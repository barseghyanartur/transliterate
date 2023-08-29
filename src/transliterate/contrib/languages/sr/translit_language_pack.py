# -*- coding: utf-8 -*-

"""
With contributions of Saša Kelečević.
"""

from transliterate.base import TranslitLanguagePack, registry
from transliterate.contrib.languages.sr import data

__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2023 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('SerbianLanguagePack',)


class SerbianLanguagePack(TranslitLanguagePack):
    """Language pack for Serbian language.

    See https://en.wikipedia.org/wiki/Romanization_of_Serbian for details.
    """
    language_code = "sr"
    language_name = "Serbian"
    character_ranges = ((0x0408, 0x04F0), (0x0000, 0x017F))
    mapping = data.mapping
    reversed_specific_mapping = data.reversed_specific_mapping
    pre_processor_mapping = data.pre_processor_mapping
    detectable = False


registry.register(SerbianLanguagePack)

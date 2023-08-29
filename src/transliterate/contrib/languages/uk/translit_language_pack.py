# -*- coding: utf-8 -*-

"""
With contributions of Timofey Pchelintsev.
"""

from transliterate.base import TranslitLanguagePack, registry
from transliterate.contrib.languages.uk import data


__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2023 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('UkrainianLanguagePack',)


class UkrainianLanguagePack(TranslitLanguagePack):
    """Language pack for Ukrainian language.

    See `http://en.wikipedia.org/wiki/Ukrainian_alphabet` for details.
    """
    language_code = "uk"
    language_name = "Ukrainian"
    character_ranges = ((0x0400, 0x04FF), (0x0500, 0x052F))
    mapping = data.mapping
    reversed_specific_mapping = data.reversed_specific_mapping
    pre_processor_mapping = data.pre_processor_mapping


registry.register(UkrainianLanguagePack)

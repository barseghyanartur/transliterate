# -*- coding: utf-8 -*-

from transliterate.base import TranslitLanguagePack, registry
from transliterate.contrib.languages.lem import data

__title__ = 'transliterate.contrib.languages.lem.translit_language_pack'
__author__ = 'Piotr Herbut'
__copyright__ = '2020 Piotr Herbut'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('LemkoLanguagePack',)


class LemkoLanguagePack(TranslitLanguagePack):
    """Language pack for Lemko language.

    See `https://pl.wikipedia.org/wiki/Język_rusiński` for details.
    REMARK 1: Transliterate to polish alphabet
    REMARK 2: Only lem -> pl actually supported correctly
    """
    language_code = "lem"
    language_name = "Lemko"
    character_ranges = ((0x0400, 0x04FF), (0x0500, 0x052F))
    mapping = data.mapping
    reversed_specific_mapping = data.reversed_specific_mapping
    pre_processor_mapping = data.pre_processor_mapping
    reversed_specific_pre_processor_mapping = data.reversed_specific_pre_processor_mapping
    detectable = True


registry.register(LemkoLanguagePack)

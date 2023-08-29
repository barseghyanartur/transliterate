# -*- coding: utf-8 -*-

"""
With contributions of Petar Chakarov.
"""

from transliterate.base import TranslitLanguagePack, registry
from transliterate.contrib.languages.bg import data

__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2023 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('BulgarianLanguagePack',)


class BulgarianLanguagePack(TranslitLanguagePack):
    """Language pack for Bulgarian language.

    See http://en.wikipedia.org/wiki/Romanization_of_Bulgarian for details.
    """
    language_code = "bg"
    language_name = "Bulgarian"
    character_ranges = ((0x0400, 0x04FF), (0x0500, 0x052F))
    mapping = data.mapping
    reversed_specific_mapping = data.reversed_specific_mapping
    pre_processor_mapping = data.pre_processor_mapping
    detectable = False


registry.register(BulgarianLanguagePack)

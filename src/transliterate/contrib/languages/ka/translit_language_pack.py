import sys

if sys.version_info < (3, 12):
    from typing_extensions import override
else:
    from typing import override

from transliterate.base import TranslitLanguagePack, registry
from transliterate.contrib.languages.ka import data

__title__ = 'transliterate.contrib.languages.ka.translit_language_pack'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2015 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('GeorgianLanguagePack',)


class GeorgianLanguagePack(TranslitLanguagePack):
    """Language pack for Georgian language.

    See `http://en.wikipedia.org/wiki/Georgian_alphabet for details.
    """
    language_code = "ka"
    language_name = "Georgian"
    character_ranges = ((0x10A0, 0x10C5), (0x10D0, 0x10FC), (0x2D00, 0x2D25))
    mapping = data.mapping
    pre_processor_mapping = data.pre_processor_mapping
    detectable = True

    @override
    def translit(
        self,
        value: str,
        reversed: bool = False,
        strict: bool = False,
        fail_silently: bool = True
    ) -> str:
        # Georgian language knows no capitals. Therefore, we convert
        # everything to lowercase.
        value = value.lower()

        # Continue the standard way
        return super().translit(
            value=value,
            reversed=reversed,
            strict=strict,
            fail_silently=fail_silently
        )


registry.register(GeorgianLanguagePack)

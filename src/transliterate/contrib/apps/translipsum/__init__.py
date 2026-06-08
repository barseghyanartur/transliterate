import sys
from typing import Any

if sys.version_info < (3, 12):
    from typing_extensions import override
else:
    from typing import override

from transliterate.contrib.apps.translipsum.utils import Generator
from transliterate.utils import translit

__title__ = 'transliterate.contrib.apps.translipsum.__init__'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('TranslipsumGenerator',)


class TranslipsumGenerator(Generator):
    """Lorem ipsum generator."""

    def __init__(self, language_code: str, reversed: bool = False, *args: Any, **kwargs: Any) -> None:  # noqa: ANN401
        self._language_code = language_code
        self._reversed = reversed
        super().__init__(*args, **kwargs)

    @override
    def generate_sentence(self, *args: Any, **kwargs: Any) -> str:  # noqa: ANN401
        """Generate sentence."""
        value = super().generate_sentence(
            *args, **kwargs
        )
        return translit(value,
                        language_code=self._language_code,
                        reversed=self._reversed)

    @override
    def generate_paragraph(self, *args: Any, **kwargs: Any) -> str:  # noqa: ANN401
        """Generate paragraph."""
        value = super().generate_paragraph(
            *args, **kwargs
        )
        return translit(value,
                        language_code=self._language_code,
                        reversed=self._reversed)

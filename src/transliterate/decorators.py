from typing import Callable, Concatenate, ParamSpec, TypeVar

from .utils import translit

__title__ = 'transliterate.decorators'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'transliterate_function',
    'transliterate_method',
)


P = ParamSpec('P')


class TransliterateFunction:
    """Function decorator."""

    language_code: str
    reversed: bool

    def __init__(self, language_code: str, reversed: bool = False) -> None:
        self.language_code = language_code
        self.reversed = reversed

    def __call__(self, func: Callable[P, str]) -> Callable[P, str]:
        def inner(*args: P.args, **kwargs: P.kwargs) -> str:
            value = func(*args, **kwargs)

            return translit(value,
                            language_code=self.language_code,
                            reversed=self.reversed)
        return inner


transliterate_function = TransliterateFunction


T = TypeVar('T')


class TransliterateMethod:
    """Method decorator."""

    def __init__(self, language_code: str, reversed: bool = False) -> None:
        self.language_code = language_code
        self.reversed = reversed

    def __call__(self, func: Callable[Concatenate[T, P], str]) -> Callable[Concatenate[T, P], str]:
        def inner(this: T, *args: P.args, **kwargs: P.kwargs) -> str:
            value = func(this, *args, **kwargs)

            return translit(value,
                            language_code=self.language_code,
                            reversed=self.reversed)
        return inner


transliterate_method = TransliterateMethod

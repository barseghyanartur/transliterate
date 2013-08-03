__title__ = 'transliterate.utils'
__version__ = '0.8'
__build__ = 0x000008
__author__ = 'Artur Barseghyan'
__all__ = ('translit', 'get_available_languages', 'detect_language', 'slugify')

import unicodedata
import re

try:
    from collections import Counter
except ImportError:
    from transliterate.backports.collections import Counter

from transliterate import autodiscover
from transliterate.base import registry
from transliterate.conf import get_setting

def ensure_autodiscover():
    """
    Ensure autodiscover.
    """
    # Running autodiscover if registry is empty
    if not registry._registry:
        autodiscover()

def translit(value, language_code, reversed=False):
    """
    Transliterates the text for the language given.

    :param str value:
    :param str language_code:
    :param bool reversed: If set to True, reversed translation is made.
    :return str:
    """
    ensure_autodiscover()

    cls = registry.get(language_code)
    language_pack = cls()
    return language_pack.translit(value, reversed=reversed)

def get_available_language_codes():
    """
    Gets list of language codes for registered language packs.

    :return list:
    """
    ensure_autodiscover()

    return registry._registry.keys()

def get_available_language_packs():
    """
    Gets list of registered language packs.

    :return list:
    """
    ensure_autodiscover()

    return registry._registry.values()

# Strips numbers from unicode string.
strip_numbers = lambda text: filter(lambda u: not u.isdigit(), text)

def extract_most_common_words(text, num_words=None):
    """
    Extracts most common words.

    :param unicode text:
    :param int num_words:
    :return list:
    """
    if num_words is None:
        num_words = get_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS')

    text = strip_numbers(text)
    counter = Counter()
    for word in text.split(' '):
        if len(word) > 1:
            counter[word] += 1
    return counter.most_common(num_words)

def detect_language(text, num_words=None):
    """
    Detects the language from the value given based on ranges defined in active language packs.

    :param unicode value: Input string.
    :param int num_words: Number of words to base decision on.
    :return str: Language code.
    """
    ensure_autodiscover()

    if num_words is None:
        num_words = get_setting('LANGUAGE_DETECTION_MAX_NUM_KEYWORDS')

    most_common_words = extract_most_common_words(text, num_words=num_words)

    counter = Counter()

    for word, occurrencies in most_common_words:
        for letter in word:
            for language_pack in get_available_language_packs():
                if language_pack.contains(letter):
                    counter[language_pack.language_code] += 1
                    continue
    try:
        return counter.most_common(1)[0][0]
    except Exception, e:
        pass

def slugify(text, language_code=None):
    """
    Slugifies the given text. If no ``language_code`` is given, autodetects the language code from text given.

    :param unicode text:
    :return str:
    """
    if not language_code:
        language_code = detect_language(text)
    if language_code:
        transliterated_text = translit(text, language_code, reversed=True)
        slug = unicodedata.normalize('NFKD', transliterated_text).encode('ascii', 'ignore').decode('ascii')
        slug = re.sub('[^\w\s-]', '', slug).strip().lower()
        return re.sub('[-\s]+', '-', slug)

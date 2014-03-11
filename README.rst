Package
==================================
transliterate

Description
==================================
Bi-directional transliterator for Python. Transliterates (unicode) strings according to the rules specified in the
language packs (source script <-> target script).

Comes with language packs for the following languages (listed in alphabetical order):

- Armenian
- Georgian (beta)
- Greek (beta)
- Russian
- Ukrainian (beta)

There are also a number of useful tools included, such as:

- Simple lorem ipsum generator, which allows lorem ipsum generation in the language chosen.
- Language detection for the text (if appropriate language pack is available).
- Slugify function for non-latin texts.

Prerequisites
==================================
- Python 2.6.8+, 2.7.+, 3.3.+

Installation
==================================
Install with latest stable version from PyPI:

    $ pip install transliterate

or install the latest stable version from bitbucket:

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/transliterate@stable#egg=transliterate

or install the latest stable version from github:

    $ pip install -e git+http://github.org/barseghyanartur/transliterate@stable#egg=transliterate

That's all. See the `Usage and examples` section for more.

Usage and examples
==================================
Simple usage
----------------------------------
Required imports

>>> from transliterate import translit, get_available_language_codes

Original text

>>> text = "Lorem ipsum dolor sit amet"

Transliteration to Armenian

>>> print translit(text, 'hy')
Լօրեմ իպսում դօլօր սիտ ամետ

Transliteration to Georgian

>>> print translit(text, 'ka')
Ⴊორემ იფსუმ დოლორ სით ამეთ

Transliteration to Greek

>>> print translit(text, 'el')
Λορεμ ιψθμ δολορ σιτ αμετ

Transliteration to Russian

>>> print translit(text, 'ru')
Лорем ипсум долор сит амет

List of available (registered) languages

>>> print get_available_language_codes()
['el', 'hy', 'ka', 'ru']

Reversed transliterations are transliterations made from target language to source language (in terms they are
defined in language packs). In case of reversed transliterations, you may leave out the ``language_code`` attribute,
although if you know it on beforehand, specify it since it works faster that way.

Reversed transliteration from Armenian

>>> print translit(u"Լօրեմ իպսում դօլօր սիտ ամետ", 'hy', reversed=True)
Lorem ipsum dolor sit amet

Reversed transliteration from Armenian with ``language_code`` argument left out

>>> print translit(u"Լօրեմ իպսում դօլօր սիտ ամետ", reversed=True)
Lorem ipsum dolor sit amet

Reversed transliteration from Georgian

>>> print translit(u"Ⴊორემ იფსუმ დოლორ სით ამეთ", 'ka', reversed=True)
Lorem ipsum dolor sit amet

Reversed transliteration from Georgian with ``language_code`` argument left out

>>> print translit(u"Ⴊორემ იფსუმ დოლორ სით ამეთ", reversed=True)
Lorem ipsum dolor sit amet

Reversed transliteration from Greek

>>> print translit(u"Λορεμ ιψθμ δολορ σιτ αμετ", 'el', reversed=True)
Lorem ipsum dolor sit amet

Reversed transliteration from Greek with ``language_code`` argument left out

>>> print translit(u"Λορεμ ιψθμ δολορ σιτ αμετ", reversed=True)
Lorem ipsum dolor sit amet

Reversed transliteration from Russian (Cyrillic)

>>> print translit(u"Лорем ипсум долор сит амет", 'ru', reversed=True)
Lorеm ipsum dolor sit amеt

Reversed transliteration from Russian (Cyrillic) with ``language_code`` argument left out

>>> print translit(u"Лорем ипсум долор сит амет", reversed=True)
Lorem ipsum dolor sit amet

Testing the decorator

>>> from transliterate.decorators import transliterate_function
>>>
>>> @transliterate_function(language_code='hy')
>>> def decorator_test(text):
>>>     return text
>>>
>>> print decorator_test(u"Lorem ipsum dolor sit amet")
Լօրեմ իպսում դօլօր սիտ ամետ

Registering a custom language pack
----------------------------------
Make sure to call the `autodiscover` function before registering your own language packs if you want to
use the bundled language packs along with your own custom ones.

>>> from transliterate.discover import autodiscover
>>> autodiscover()

Then the custom language pack part comes.

>>> from transliterate.base import TranslitLanguagePack, registry
>>>
>>> class ExampleLanguagePack(TranslitLanguagePack):
>>>     language_code = "example"
>>>     language_name = "Example"
>>>     mapping = (
>>>         u"abcdefghij",
>>>         u"1234567890",
>>>     )
>>>
>>> registry.register(ExampleLanguagePack)
>>>
>>> print get_available_language_codes()
['el', 'hy', 'ka', 'ru', 'example']
>>> 
>>> print translit(text, 'example')
Lor5m 9psum 4olor s9t 1m5t

It's possible to replace existing language packs with your own ones. By default, existing language packs are not
force-installed.

To force install a language pack, set the ``force`` argument to True when registering a language pack. In that 
case, if a language pack with same language code has already been registered, it will be replaced; otherwise, if
language pack didn't exist in the registry, it will be just registered.

>>> registry.register(ExampleLanguagePack, force=True)

Forced language packs can't be replaced or unregistered.

Using the lorem ipsum generator
----------------------------------
Note, that due to incompatibility of the original `lorem-ipsum-generator` package with Python 3, when used
with Python 3 `transliterate` uses its' own simplified fallback lorem ipsum generator (which still does the job).

Required imports

>>> from transliterate.contrib.apps.translipsum import TranslipsumGenerator

Generating paragraphs in Armenian

>>> g_am = TranslipsumGenerator(language_code='hy')
>>> print g_am.generate_paragraph()
Մագնա տրիստիքուե ֆաուցիբուս ֆամես նետուս նետուս օրցի մաուրիս, սուսցիպիտ. Դապիբուս րիսուս սեդ ադիպիսցինգ դիցտում.
Ֆերմենտում ուրնա նատօքուե ատ. Uլտրիցես եգետ, տացիտի. Լիտօրա ցլասս ցօնուբիա պօսուերե մալեսուադա ին իպսում իդ պեր վե. 

Generating sentense in Georgian

>>> g_ka = TranslipsumGenerator(language_code='ka')
>>> print g_ka.generate_sentence()
Ⴄგეთ ყუამ არcუ ვულფუთათე რუთრუმ აუcთორ.

Generating sentense in Greek

>>> g_el = TranslipsumGenerator(language_code='el')
>>> print g_el.generate_sentence()
Νεc cρασ αμετ, ελιτ vεστιβθλθμ εθ, αενεαν ναμ, τελλθσ vαριθσ.

Generating sentense in Russian (Cyrillic)

>>> g_ru = TranslipsumGenerator(language_code='ru')
>>> print g_ru.generate_sentence()
Рисус cонсеcтетуер, фусcе qуис лаореет ат ерос пэдэ фелис сенеcтус, магна.

Language detection
----------------------------------
Required imports

>>> from transliterate import detect_language

Detect Armenian text

>>> detect_language(u'Լօրեմ իպսում դօլօր սիտ ամետ')
hy

Detect Georgian text

>>> detect_language(u'Ⴊორემ იფსუმ დოლორ სით ამეთ')
ka

Detect Greek text

>>> detect_language(u'Λορεμ ιψθμ δολορ σιτ αμετ')
el

Detect Russian (Cyrillic) text

>>> detect_language(u'Лорем ипсум долор сит амет')
ru

Slugify
----------------------------------
Required imports

>>> from transliterate import slugify

Slugify Armenian text

>>> slugify(u'Լօրեմ իպսում դօլօր սիտ ամետ')
lorem-ipsum-dolor-sit-amet

Slugify Georgian text

>>> slugify(u'Ⴊორემ იფსუმ დოლორ სით ამეთ')
lorem-ipsum-dolor-sit-amet

Slugify Greek text

>>> slugify(u'Λορεμ ιψθμ δολορ σιτ αμετ')
lorem-ipsum-dolor-sit-amet

Slugify Russian (Cyrillic) text

>>> slugify(u'Лорем ипсум долор сит амет')
lorem-ipsum-dolor-sit-amet

Missing a language pack?
==================================
Missing a language pack for your own language? Contribute to the project by making one and it will appear in a new
version (which will be released very quickly).

License
==================================
GPL 2.0/LGPL 2.1

Support
==================================
For any issues contact me at the e-mail given in the `Author` section.

Author
==================================
Artur Barseghyan <artur.barseghyan@gmail.com>

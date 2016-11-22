=============
transliterate
=============
Bi-directional transliterator for Python. Transliterates (unicode) strings
according to the rules specified in the language packs (source script <->
target script).

Comes with language packs for the following languages (listed in alphabetical
order):

- Armenian
- Bulgarian (beta)
- Georgian
- Greek
- Macedonian (alpha)
- Mongolian (alpha)
- Russian
- Ukrainian (beta)

There are also a number of useful tools included, such as:

- Simple lorem ipsum generator, which allows lorem ipsum generation in the
  language chosen.
- Language detection for the text (if appropriate language pack is available).
- Slugify function for non-latin texts.

Prerequisites
=============
- Python 2.6.8+, 2.7.+, 3.3.+

Installation
============
Install with latest stable version from PyPI.

.. code-block:: sh

    $ pip install transliterate

or install the latest stable version from bitbucket:

.. code-block:: sh

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/transliterate@stable#egg=transliterate

or install the latest stable version from github:

.. code-block:: sh

    $ pip install -e git+http://github.org/barseghyanartur/transliterate@stable#egg=transliterate

That's all. See the `Usage and examples` section for more.

Usage and examples
==================
Simple usage
------------
Required imports

.. code-block:: python

    from transliterate import translit, get_available_language_codes

Original text

.. code-block:: python

    text = "Lorem ipsum dolor sit amet"

Transliteration to Armenian

.. code-block:: python

    print translit(text, 'hy')

    # Output: Լօրեմ իպսում դօլօր սիտ ամետ

Transliteration to Georgian

.. code-block:: python

    print translit(text, 'ka')

    # Output: Ⴊორემ იფსუმ დოლორ სით ამეთ

Transliteration to Greek

.. code-block:: python

    print translit(text, 'el')

    # Output: Λορεμ ιψθμ δολορ σιτ αμετ

Transliteration to Russian

.. code-block:: python

    print translit(text, 'ru')

    # Output: Лорем ипсум долор сит амет

List of available (registered) languages

.. code-block:: python

    print get_available_language_codes()

    # Output: ['el', 'hy', 'ka', 'ru']

Reversed transliterations are transliterations made from target language to
source language (in terms they are defined in language packs). In case of
reversed transliterations, you may leave out the ``language_code`` attribute,
although if you know it on beforehand, specify it since it works faster that
way.

Reversed transliteration from Armenian

.. code-block:: python

    print translit(u"Լօրեմ իպսում դօլօր սիտ ամետ", 'hy', reversed=True)

    # Output: Lorem ipsum dolor sit amet

Reversed transliteration from Armenian with ``language_code`` argument left out

.. code-block:: python

    print translit(u"Լօրեմ իպսում դօլօր սիտ ամետ", reversed=True)

    # Output: Lorem ipsum dolor sit amet

Reversed transliteration from Georgian

.. code-block:: python

    print translit(u"Ⴊორემ იფსუმ დოლორ სით ამეთ", 'ka', reversed=True)

    # Output: Lorem ipsum dolor sit amet

Reversed transliteration from Georgian with ``language_code`` argument left out

.. code-block:: python

    print translit(u"Ⴊორემ იფსუმ დოლორ სით ამეთ", reversed=True)

    # Output: Lorem ipsum dolor sit amet

Reversed transliteration from Greek

.. code-block:: python

    print translit(u"Λορεμ ιψθμ δολορ σιτ αμετ", 'el', reversed=True)

    # Output: Lorem ipsum dolor sit amet

Reversed transliteration from Greek with ``language_code`` argument left out

.. code-block:: python

    print translit(u"Λορεμ ιψθμ δολορ σιτ αμετ", reversed=True)

    # Output: Lorem ipsum dolor sit amet

Reversed transliteration from Russian (Cyrillic)

.. code-block:: python

    print translit(u"Лорем ипсум долор сит амет", 'ru', reversed=True)

    # Output: Lorеm ipsum dolor sit amеt

Reversed transliteration from Russian (Cyrillic) with ``language_code``
argument left out

.. code-block:: python

    print translit(u"Лорем ипсум долор сит амет", reversed=True)

    # Output: Lorem ipsum dolor sit amet

Testing the decorator

.. code-block:: python

    from transliterate.decorators import transliterate_function

    @transliterate_function(language_code='hy')
    def decorator_test(text):
        return text

    print decorator_test(u"Lorem ipsum dolor sit amet")

    # Output: Լօրեմ իպսում դօլօր սիտ ամետ

Registering a custom language pack
----------------------------------
Basics
~~~~~~
Make sure to call the `autodiscover` function before registering your own
language packs if you want to use the bundled language packs along with your
own custom ones.

.. code-block:: python

    from transliterate.discover import autodiscover
    autodiscover()

Then the custom language pack part comes.

.. code-block:: python

    from transliterate.base import TranslitLanguagePack, registry

    class ExampleLanguagePack(TranslitLanguagePack):
        language_code = "example"
        language_name = "Example"
        mapping = (
            u"abcdefghij",
            u"1234567890",
        )

    registry.register(ExampleLanguagePack)

    print get_available_language_codes()

    # Output: ['el', 'hy', 'ka', 'ru', 'example']

    print translit(text, 'example')

    # Output: Lor5m 9psum 4olor s9t 1m5t

It's possible to replace existing language packs with your own ones. By
default, existing language packs are not force-installed.

To force install a language pack, set the ``force`` argument to True when
registering a language pack. In that case, if a language pack with same
language code has already been registered, it will be replaced; otherwise,
if language pack didn't exist in the registry, it will be just registered.

.. code-block:: python

    registry.register(ExampleLanguagePack, force=True)

Forced language packs can't be replaced or unregistered.

API in depth
~~~~~~~~~~~~
There are 7 class properties that you could/should be using in your language
pack, of which 4 are various sorts of mappings.

Mappings
++++++++

- ``mapping`` (tuple): A tuple of two strings, that simply represent the 
  mapping of characters from the source language to the target language. For
  example, if your source language is Latin and you want to convert "a", "b",
  "c", "d" and "e" characters to appropriate characters in Russian Cyrillic,
  your mapping would look as follows:

  .. code-block:: python

        mapping = (u"abcde", u"абцде")

  Example (taken from the Greek language pack).

  .. code-block:: python
  
        mapping = (
            u"abgdezhiklmnxoprstyfwuABGDEZHIKLMNXOPRSTYFWU",
            u"αβγδεζηικλμνξοπρστυφωθΑΒΓΔΕΖΗΙΚΛΜΝΞΟΠΡΣΤΥΦΩΘ",
        )

- ``reversed_specific_mapping`` (tuple): When making reversed translations,
  the ``mapping`` property is still used, but in some cases you need to provide
  additional rules. This property (``reversed_specific_mapping``) is meant for
  such cases. Further, is alike the ``mapping``.

  Example (taken from the Greek language pack).

  .. code-block:: python

        reversed_specific_mapping = (
            u"θΘ",
            u"uU"
        )

- ``pre_processor_mapping`` (dict): A dictionary of mapping from source
  language to target language. Use this only in cases if a single character
  in source language shall be represented by more than one character in the
  target language.

  Example (taken from the Greek language pack).

  .. code-block:: python
  
        pre_processor_mapping = {
            u"th": u"θ",
            u"ch": u"χ",
            u"ps": u"ψ",
            u"TH": u"Θ",
            u"CH": u"Χ",
            u"PS": u"Ψ",
        }

- ``reversed_specific_pre_processor_mapping``: Same as
  ``pre_processor_mapping``, but used in reversed translations.

  Example (taken from the Armenian language pack)

  .. code-block:: python

        reversed_specific_pre_processor_mapping = {
            u"ու": u"u",
            u"Ու": u"U"
        }

Additional
++++++++++
- ``character_ranges`` (tuple): A tuple of character ranges (unicode table).
  Used in language detection. Works only if ``detectable`` property is set
  to True. Be aware, that language (or shall I better be saying - script) 
  detection is very basic and is based on characters only.

- ``detectable`` (bool): If set to True, language pack would be used
  for automatic language detection.

Using the lorem ipsum generator
-------------------------------
Note, that due to incompatibility of the original `lorem-ipsum-generator`
package with Python 3, when used with Python 3 `transliterate` uses its' own
simplified fallback lorem ipsum generator (which still does the job).

Required imports

.. code-block:: python

    from transliterate.contrib.apps.translipsum import TranslipsumGenerator

Generating paragraphs in Armenian

.. code-block:: python

    g_am = TranslipsumGenerator(language_code='hy')
    print g_am.generate_paragraph()

    # Output: Մագնա տրիստիքուե ֆաուցիբուս ֆամես նետուս նետուս օրցի մաուրիս,
    # սուսցիպիտ. Դապիբուս րիսուս սեդ ադիպիսցինգ դիցտում. Ֆերմենտում ուրնա
    # նատօքուե ատ. Uլտրիցես եգետ, տացիտի. Լիտօրա ցլասս ցօնուբիա պօսուերե
    # մալեսուադա ին իպսում իդ պեր վե.

Generating sentense in Georgian

.. code-block:: python

    g_ka = TranslipsumGenerator(language_code='ka')
    print g_ka.generate_sentence()

    # Output: Ⴄგეთ ყუამ არcუ ვულფუთათე რუთრუმ აუcთორ.

Generating sentense in Greek

.. code-block:: python

    g_el = TranslipsumGenerator(language_code='el')
    print g_el.generate_sentence()

    # Output: Νεc cρασ αμετ, ελιτ vεστιβθλθμ εθ, αενεαν ναμ, τελλθσ vαριθσ.

Generating sentense in Russian (Cyrillic)

.. code-block:: python

    g_ru = TranslipsumGenerator(language_code='ru')
    print g_ru.generate_sentence()

    # Output: Рисус cонсеcтетуер, фусcе qуис лаореет ат ерос пэдэ фелис магна.

Language detection
------------------
Required imports

.. code-block:: python

    from transliterate import detect_language

Detect Armenian text

.. code-block:: python

    detect_language(u'Լօրեմ իպսում դօլօր սիտ ամետ')

    # Output: hy

Detect Georgian text

.. code-block:: python

    detect_language(u'Ⴊორემ იფსუმ დოლორ სით ამეთ')

    # Output: ka

Detect Greek text

.. code-block:: python

    detect_language(u'Λορεμ ιψθμ δολορ σιτ αμετ')

    # Output: el

Detect Russian (Cyrillic) text

.. code-block:: python

    detect_language(u'Лорем ипсум долор сит амет')

    # Output: ru

Slugify
-------
Required imports

.. code-block:: python

    from transliterate import slugify

Slugify Armenian text

.. code-block:: python

    slugify(u'Լօրեմ իպսում դօլօր սիտ ամետ')

    # Output: lorem-ipsum-dolor-sit-amet

Slugify Georgian text

.. code-block:: python

    slugify(u'Ⴊორემ იფსუმ დოლორ სით ამეთ')

    # Output: lorem-ipsum-dolor-sit-amet

Slugify Greek text

.. code-block:: python

    slugify(u'Λορεμ ιψθμ δολορ σιτ αμετ')

    # Output: lorem-ipsum-dolor-sit-amet

Slugify Russian (Cyrillic) text

.. code-block:: python

    slugify(u'Лорем ипсум долор сит амет')

    # Output: lorem-ipsum-dolor-sit-amet

Missing a language pack?
========================
Missing a language pack for your own language? Contribute to the project by
making one and it will appear in a new version (which will be released very
quickly).

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author` section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>

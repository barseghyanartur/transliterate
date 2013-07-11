Package
==================================
transliterate

Description
==================================
Transliterator for Python. Transliterates (unicode) strings according to the rules specified in the language packs.

Comes with language packs for the following languages (listed in alphabetical order):

- Armenian
- Russian

There's also a simple lorem ipsum generator included, which allows lorem ipsum generation in the language chosen.

Installation
==================================
Install with latest stable version from pypi:

    $ pip install transliterate

or install the latest stable version from source:

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/transliterate@stable#egg=transliterate

or install into python path:

    $ python setup.py install

That's all. See the `Usage and examples` section for more.

Usage and examples
==================================
Simple usage
----------------------------------
Required imports

>>> from transliterate import autodiscover
>>> from transliterate.utils import translit, get_available_languages

Autodiscover installed available language packs

>>> autodiscover()

Original text

>>> text = "Lorem ipsum dolor sit amet"

Transliteration to Armenian

>>> print translit(text, 'hy')
Լօրեմ իպսում դօլօր սիտ ամետ

Transliteration to Russian

>>> print translit(text, 'ru')
Лорэм ипсум долор сит амэт

List of available (registered) languages

>>> print get_available_languages()
['ru', 'hy']

Reversed transliteration from Armenian

>>> text = "Լօրեմ իպսում դօլօր սիտ ամետ"
>>> print translit(text, 'hy', reversed=True)
Lorem ipsum dolor sit amet

Reversed transliteration from Russian

>>> text = "Лорем ипсум долор сит амет"
>>> print translit(text, 'ru', reversed=True)
Lorеm ipsum dolor sit amеt

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
>>> print get_available_languages()
['ru', 'hy', 'example']
>>> 
>>> print translit(text, 'example')
Lor5m 9psum 4olor s9t 1m5t

Using the lorem ipsum generator
----------------------------------
Required imports

>>> from transliterate.contrib.apps.translipsum import TranslipsumGenerator

Generating paragraphs

>>> g_am = TranslipsumGenerator(language_code='hy')
>>> print g_am.generate_paragraph()
Մագնա տրիստիքուե ֆաուցիբուս ֆամես նետուս նետուս օրցի մաուրիս, սուսցիպիտ. Դապիբուս րիսուս սեդ ադիպիսցինգ դիցտում.
Ֆերմենտում ուրնա նատօքուե ատ. Uլտրիցես եգետ, տացիտի. Լիտօրա ցլասս ցօնուբիա պօսուերե մալեսուադա ին իպսում իդ պեր վե. 

Generating sentense

>>> g_ru = TranslipsumGenerator(language_code='ru')
>>> print g_ru.generate_sentence()
Рисус cонсэcтэтуэр, фусcэ qуис лаорээт ат эрос пэдэ фэлис сэнэcтус, магна.

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

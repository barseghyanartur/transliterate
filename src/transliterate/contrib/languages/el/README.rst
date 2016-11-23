==================================
transliterate.contrib.languages.el
==================================
Transliterate language pack for Greek language.

See `Greek alphabet <http://en.wikipedia.org/wiki/Greek_alphabet>`_ and
`Romanization of Greek
<https://en.wikipedia.org/wiki/Romanization_of_Greek#Modern_Greek>`_ for
details.

Useful to know
==============
Excerpt from a `github issue
<https://github.com/barseghyanartur/transliterate/pull/17>`_:

.. code-block:: text

The 'ϑ' (the Greek theta symbol, http://unicode-table.com/en/03D1/) is not
really used as a letter (as in I haven't seen a text containing it in prose
in my whole life) in Modern Greek, at least in non handwritten
text (handwritten text is so subjective, we probably should totally avoid
discussing). The letter used in everyday text
is 'θ' (http://unicode-table.com/en/03B8/). The most probable reason for
this (and one that is semantically correct) is that Greek keyboard layouts
will not emit 'ϑ' in any easy way but will emit 'θ'. Writing the symbol form
requires either copy pasting, knowing the keyboard unicode key sequence or
using a specialized program.

'ϑ' is used as a mathematical symbol. While using the letter form ('θ') in
mathematics is acceptable, some mathematics professors encourage students to
distinguish between 'ϑ' and 'θ' (even in handwriting) without however strongly
enforcing the distinction (as in penalizing students for not using the correct
form).

So, your comment is correct with the caveat that if this library is ever used
to transliterate a text (like a mathematical one or even this comment)
conveying meaning via the use of the symbol, that meaning will be lost. Which
is practically fine, I think.

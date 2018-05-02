TODOs
=====
Based on MoSCoW principle

Must haves
----------
- Prediction/auto-suggest feature.
- Make the API documentation really obvious. Explain in detail what is ``mapping``,
  ``pre_processor_mapping`` and ``reversed_specific_mapping``, as well as other
  properties and methods, which are possible to tweak/override. Explain more about
  ``detectable`` property of the language pack and on the example of Ukrainian
  language pack, explain what to do with languages that do have same scripts (use
  same unicode characters). Add examples on Ukrainian language pack into the main
  readme.
- Command line tool for transliterating files (source language, target language, 
  source file, target file).
- Implement stripping out of the symbols.
- Check and make appropriate fixes (if necessary) to the Greek pack. Quote """
    I also find an error in your "el" Greek file. Both "y" and "u" should go to
    upsilon "υ", not "u" into theta "θ", and "w" doesn't really go to anything,
    although "υ" would be the closest.
    It does not work to always transliterate "ps" into "ψ", because in a word
    like "ipsum" their roots dictate "υπσυμ" would be better.

Should haves
------------
- Japanese support.

Could haves
-----------

Would haves
-----------

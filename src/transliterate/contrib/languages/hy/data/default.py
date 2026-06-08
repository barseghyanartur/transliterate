__title__ = 'transliterate.contrib.languages.hy.data.default'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'mapping',
    'reversed_specific_mapping',
    'reversed_specific_pre_processor_mapping',
    'pre_processor_mapping',
)

mapping = (
    "abgdezilxkhmjnpsvtrcq&ofABGDEZILXKHMJNPSVTRCQOF",
    "աբգդեզիլխկհմյնպսվտրցքևօֆԱԲԳԴԵԶԻԼԽԿՀՄՅՆՊՍՎՏՐՑՔՕՖ",
)
reversed_specific_mapping = (
    "ռՌ",
    "rR"
)
reversed_specific_pre_processor_mapping = {
    "ու": "u",
    "Ու": "U"
}
pre_processor_mapping = {
    # lowercase
    "e'": "է",
    "y": "ը",
    "th": "թ",
    "jh": "ժ",
    "ts": "ծ",
    "dz": "ձ",
    "gh": "ղ",
    "tch": "ճ",
    "sh": "շ",
    "vo": "ո",
    "ch": "չ",
    "dj": "ջ",
    "ph": "փ",
    "u": "ու",

    # uppercase
    "E'": "Է",
    "Y": "Ը",
    "Th": "Թ",
    "Jh": "Ժ",
    "Ts": "Ծ",
    "Dz": "Ձ",
    "Gh": "Ղ",
    "Tch": "Ճ",
    "Sh": "Շ",
    "Vo": "Ո",
    "Ch": "Չ",
    "Dj": "Ջ",
    "Ph": "Փ",
    "U": "Ու"
}

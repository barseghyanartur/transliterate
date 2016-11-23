# -*- coding: utf-8 -*-

mapping = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHILJKMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyzABCDEFGHILJKMNOPQRSTUVWXYZ",
)

reversed_specific_mapping = (
    "àÀáÁâÂãÃèÈéÉêÊëËìÌíÍîÎïÏðÐñÑòÒóÓôÔõÕùÙúÚûÛýÝÿŸ",
    "aAaAaAaAeEeEeEeEiIiIiIiIdDnNoOoOoOaOuUuUuUyYyY",
)

reversed_specific_pre_processor_mapping = {
    "å": "aa",
    "Å": "Aa",
    "ä": "ae",
    "Ä": "Ae",
    "æ": "ae",
    "Æ": "Ae",
    "Ç": "Ts",
    "ç": "ts",
    "ð": "dh",
    "ö": "oe",
    "Ö": "Oe",
    "ø": "oe",
    "Ø": "Oe",
    "ü": "ue",
    "Ü": "Ue",
    "þ": "th",
    "Þ": "Th",
    "ß": "ss",
}

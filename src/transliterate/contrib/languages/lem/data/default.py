# -*- coding: utf-8 -*-

mapping = (
    u"abwghdezijkłmnoprstufcyŷżABWGHDEZIJKŁMNOPRSTUFCYŶŻ",
    u"абвґгдезійклмнопрстуфциыжАБВҐГДЕЗІЙКЛМНОПРСТУФЦИЫЖ",
)

reversed_specific_mapping = ( 
    u"",
    u""
)

pre_processor_mapping = {}

reversed_specific_pre_processor_mapping = {
    u"цьо": u"cio",
    u"Цьо": u"Cio",
    u"ньо": u"nio",
    u"Ньо": u"Nio",
    u"сьo": u"sio",
    u"Сьo": u"Sio",
    u"зьo": u"zio",
    u"Зьo": u"Zio",
    #REVISIT: handle ю,я,є after vovel better
    u"бє": u"biе",
    u"бю": u"biu",
    u"бя": u"biа",
    u"Бє": u"Biе",
    u"Бю": u"Biu",
    u"Бя": u"Biа",
    u"вє": u"wiе",
    u"вю": u"wiu",
    u"вя": u"wiа",
    u"Вє": u"Wiе",
    u"Вю": u"Wiu",
    u"Вя": u"Wiа",
    u"ґє": u"giе",
    u"ґю": u"giu",
    u"ґя": u"giа",
    u"Ґє": u"Giе",
    u"Ґю": u"Giu",
    u"Ґя": u"Giа",
    u"гє": u"hiе",
    u"гю": u"hiu",
    u"гя": u"hiа",
    u"Гє": u"Hiе",
    u"Гю": u"Hiu",
    u"Гя": u"Hiа",
    u"дє": u"diе",
    u"дю": u"дiu",
    u"дя": u"diа",
    u"Дє": u"Diе",
    u"Дю": u"Diu",
    u"Дя": u"Diа",
    u"зє": u"ziе",
    u"зю": u"ziu",
    u"зя": u"ziа",
    u"Зє": u"Ziе",
    u"Зю": u"Ziu",
    u"Зя": u"Ziа",
    u"кє": u"kiе",
    u"кю": u"kiu",
    u"кя": u"kiа",
    u"Кє": u"Kiе",
    u"Кю": u"Kiu",
    u"Кя": u"Kiа",
    u"ле": u"le",
    u"лє": u"lie",
    u"лю": u"lu",
    u"ля": u"la",
    u"Ле": u"Le",
    u"Лє": u"Lie",
    u"Лю": u"Lu",
    u"Ля": u"La",
    u"мє": u"miе",
    u"мю": u"miu",
    u"мя": u"miа",
    u"Мє": u"Miе",
    u"Мю": u"Miu",
    u"Мя": u"Miа",
    u"нє": u"niе",
    u"ню": u"niu",
    u"ня": u"niа",
    u"Нє": u"Niе",
    u"Ню": u"Niu",
    u"Ня": u"Niа",
    u"пє": u"piе",
    u"пю": u"piu",
    u"пя": u"piа",
    u"Пє": u"Piе",
    u"Пю": u"Piu",
    u"Пя": u"Piа",
    u"рє": u"riе",
    u"рю": u"riu",
    u"ря": u"riа",
    u"Рє": u"Riе",
    u"Рю": u"Riu",
    u"Ря": u"Riа",
    u"сє": u"siе",
    u"сю": u"siu",
    u"ся": u"siа",
    u"Сє": u"Siе",
    u"Сю": u"Siu",
    u"Ся": u"Siа",
    u"тє": u"tiе",
    u"тю": u"tiu",
    u"тя": u"tiа",
    u"Тє": u"Tiе",
    u"Тю": u"Tiu",
    u"Тя": u"Tiа",
    u"фє": u"fiе",
    u"фю": u"fiu",
    u"фя": u"fiа",
    u"Фє": u"Fiе",
    u"Фю": u"Fiu",
    u"Фя": u"Fiа",
    u"цє": u"ciе",
    u"цю": u"ciu",
    u"ця": u"ciа",
    u"Цє": u"Ciе",
    u"Цю": u"Ciu",
    u"Ця": u"Ciа",
    u"жє": u"żiе",
    u"жю": u"żiu",
    u"жя": u"żiа",
    u"Жє": u"Żiе",
    u"Жю": u"Żiu",
    u"Жя": u"Żiа",
    u"хє": u"Chiе",
    u"хю": u"Chiu",
    u"хя": u"Chiа",
    u"Хє": u"Chiе",
    u"Хю": u"Chiu",
    u"Хя": u"Chiа",
    u"чє": u"Cziе",
    u"чю": u"Cziu",
    u"чя": u"Cziа",
    u"Чє": u"Cziе",
    u"Чю": u"Cziu",
    u"Чя": u"Cziа",
    u"шє": u"sziе",
    u"шю": u"sziu",
    u"шя": u"sziа",
    u"Шє": u"Sziе",
    u"Шю": u"Sziu",
    u"Шя": u"Sziа",
    u"щє": u"szcziе",
    u"щю": u"szcziu",
    u"щя": u"szcziа",
    u"Щє": u"Szcziе",
    u"Щю": u"Szcziu",
    u"Щя": u"Szcziа",
    #END ю,я,є after vovel better
    u"ць": u"ć",
    u"Ць": u"Ć",
    u"ль": u"l",
    u"Ль": u"L",
    u"нь": u"ń",
    u"Нь": u"Ń",
    u"сь": u"ś",
    u"Сь": u"Ś",
    u"зь": u"ź",
    u"Зь": u"Ź",
    u"ч": u"cz",
    u"Ч": u"Cz",
    u"х": u"ch",
    u"Х": u"Ch",
    u"ш": u"sz",
    u"Ш": u"Sz",
    u"щ": u"szcz",
    u"Щ": u"Szcz",
    u"є": u"jе",
    u"Є": u"Jе",
    u"ї": u"ji",
    u"Ї": u"Ji",
    u"я": u"ja",
    u"Я": u"Ja",
    u"ю": u"ju",
    u"Ю": u"Ju",
    u"ъ": u"'",
    u"ъ": u"'",
    u"ь": u"`",
    u"Ь": u"`"
}
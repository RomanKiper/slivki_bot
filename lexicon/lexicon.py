LEXICON_COMMANDS: dict[str, str] = {
    '/main_menu': 'ГЛАВНОЕ МЕНЮ',
    '/admin': 'АДМИНКА',
}

LEXICON_HI = {"привет", "здорова", "хай", "приветствую", "добрый день", "здравствуйте", "здрасти", "hi", "hello",
               "good morning", "good day"}

restricted_words = {'дурак', 'осел', 'болван', 'пидор', 'сидор', 'хуй'}


LEXICON_RU: dict[str, str] = {
    '/start': 'привет!✌\nЯ Bun_bot😎! Моя задача помочь тебе в работе со Сликами Бай.\n\n'
              'Я дам тебе:\n'
              '✅Варианты размещения на Сливках.\n'
              '✅Стоимость.\n'
              '✅Статистику.\n'
              '✅Примеры.\n\n'
              'Если хочешь узнать какие команды доступны тебе, отправь команду /help\n'
              'Ты можешь воспользваться основным меню!\n'
              '👇👇👇 Меню.',

    '/help': 'Тебе доступны команды:\n'
             '/start - запуск бота.\n'
             '/help - список команд.\n'
             '/description - описание бота.\n'
             '/insta_links - список ссылок на каналы instagram.\n'
             '/tiktok_links - список ссылок на каналы TikTok.\n'
             'Ты можешь воспользваться основным меню!\n'
             '👇👇👇 Меню.'
    ,
    '/description_slivki':
        '<b>Сливки бай - это крупнейший маркетплэйс скидок в РБ.</b>\n'
        '✅13 лет на рынке услуг.\n'
        '✅1 000 000+ пользователей на сайте в месяц.\n'
        '✅1 000 000+ установок приложения.\n'
        '✅756 000+ подписчиков в социальных медиа.\n'
        '✅11 000+ партнеров.\n'
        '✅15 Instagram-каналов в РБ.\n'
        '✅30 блогеров в штате.\n'
        '✅40 городов в Беларуси.\n\n'
        '👨‍👨‍👧‍👦Аудитория Сливки Бай - активное население Беларуси со средним доходом и с яркой жизненной позицией.\n'
    ,

    '/office_adress':
        "Адрес:\nг.Минск, Центральный район, Победителей проспект. 7а.\n"
        "Бизнес-центр Royal Plaza (Роял Плаза).\n"
        "29 - 30 этаж.\n",

    '/description': '😎Bun_bot - вертуальный специалит по качественному продвижению в компании Сливки бай.\n'
                    '😎Bun_bot даст вам  цены на услуги компании, статистику, покажет примеры,'
                    ' ознакомит вас с основными вариантами размещения на Сливках.\n'
                    '😎Bun_bot является молодым ботом. Он будет развиваться, а объем и качество, предоставляемой им информации, будут расти.'
    ,

    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',

    '/insta_links': '<b>Ссылки на каналы Instagram:</b>\n'
                    '<a href="https://www.instagram.com/slivkiby">www.instagram.com/slivkiby</a>\n'
                    '<a href="https://www.instagram.com/giperspros">www.instagram.com/giperspros</a>\n'
                    '<a href="https://www.instagram.com/slivkiby_brest">www.instagram.com/slivkiby_brest</a>\n'
                    '<a href="https://www.instagram.com/slivkiby_gomel">www.instagram.com/slivkiby_gomel</a>\n'
                    '<a href="https://www.instagram.com/slivkiby_mogilev">www.instagram.com/slivkiby_mogilev</a>\n'
                    '<a href="https://www.instagram.com/slivki_grodno">www.instagram.com/slivki_grodno</a>\n'
                    '<a href="https://www.instagram.com/slivkiby_vitebsk">www.instagram.com/slivkiby_vitebsk</a>\n'
                    '<a href="https://www.instagram.com/slivkiby_svetlogorsk">www.instagram.com/slivkiby_svetlogorsk</a>\n'
                    '<a href="https://www.instagram.com/slivkiby_pinsk">www.instagram.com/slivkiby_pinsk</a>\n'
                    '<a href="https://www.instagram.com/slivkiby_bobruisk">www.instagram.com/slivkiby_bobruisk</a>\n'
                    '<a href="https://www.instagram.com/slivki_baranovichi">www.instagram.com/slivki_baranovichi</a>\n'
                    '<a href="https://www.instagram.com/slivki_borisov">www.instagram.com/slivki_borisov</a>\n'
                    '<a href="https://www.instagram.com/slivkiby_orsha">www.instagram.com/slivkiby_orsha</a>\n'
    ,

    '/tiktok_links': '<b>Ссылки на каналы TikTok:</b>\n'
                     '<a href="https://www.tiktok.com/@slivkiby">www.tiktok.com/@slivkiby</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_brest">www.tiktok.com/@slivkiby_brest</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_vitebsk">www.tiktok.com/@slivkiby_vitebsk</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_grodno">www.tiktok.com/@slivkiby_grodno</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_gomel">www.tiktok.com/@slivkiby_gomel</a>\n'
                     '<a href="https://www.tiktok.com/@slivkimogilev">www.tiktok.com/@slivkimogilev</a>\n'
                     '<a href="https://www.tiktok.om/@slivkiby_bobruysk">www.tiktok.om/@slivkiby_bobruysk</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_borisov">www.tiktok.com/@slivkiby_borisov</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_baranovichi">www.tiktok.com/@slivkiby_baranovichi</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_pinsk">www.tiktok.com/@slivkiby_pinsk</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_svetlogorsk">www.tiktok.com/@slivkiby_svetlogorsk</a>\n'
                     '<a href="https://www.tiktok.com/@slivkiby_orsha">www.tiktok.com/@slivkiby_orsha</a>\n'
    ,
    '/list_links_work_tables': '<b>Рабочие таблицы/регламенты(только для работкников  Slivkiby):</b>\n\n'
                               '<a href="https://docs.google.com/spreadsheets/d/13lJebGgLptSelDHMcb_-QWP3SfQQ2TNry1td0qFTPBk/edit#gid=654343601">Таблица инстаграм.</a>\n\n'
                               '<a href="https://docs.google.com/spreadsheets/d/1BWHJ3xwKwhtMKApPSwXHpF2s2wifQ1Xregtj7zfaJ1A/edit#gid=1293730834">Дневные отчеты/посещаемость.</a>\n\n'
                               '<a href="https://docs.google.com/spreadsheets/d/1hHsBoWh8uM9ENREd2ARvIxlH0AwcYuH6PcxrCDDbiXw/edit?userstoinvite=roman@slivki.by&sharingaction=manageaccess&role=writer#gid=443600561">Большая таблица.</a>\n\n'
                               '<a href="https://docs.google.com/document/d/12wgVsiGgn-3IuwG3n2p7RpEgN69u_-7d9w60vk3KubQ/edit?pli=1#heading=h.6vbdo72hsqbe">Условия работы/регламенты.</a>\n\n'

}

LEXICON_btn_main_menu: dict[str, str] = {
    'btn_main_menu_2': '👨‍🎤Блогеры',
    'btn_main_menu_3': 'Сливки это',
    'btn_main_menu_4': 'FAQ🤯',
    'btn_main_menu_5': 'Наш адрес',
    'btn_contract_links': 'Договоры',
    'download_app': 'Приложение',
    'btn_main_menu_1': 'Цены/статистика',
}

LEXICON_btn_employee_menu: dict[str, str] = {
    'tables_links': 'Рабочие таблицы',
    'work_links': 'Рабочие ссылки',
    'offer_online': 'Создать КП',
    'admin': 'Админка',
}

LEXICON_btn_price_statistic: dict[str, str] = {
    'site_slivki_advertising': 'Сайт/реклама',
    'site_slivki_promotion': 'Сайт/акция🔥',
    'instagram_sl': 'Instagram',
    'telegram_sl': 'Telegram',
    'tiktok_sl': 'TikTok',
    'app_advertising': 'Приложение',
    'reviews': 'Обзоры/примеры',
    'main_menu': 'Назад в меню',
}

LEXICON_btn_reviews: dict[str, str] = {
    'review_bilding': 'Стройматериалы',
    'review_cars': 'Автомобили',
    'review_electronics': 'Эл.техика',
    'review_beauty': 'Бьюти',
    'review_food': 'Еда',
    'review_relax': 'Отдых',
    'btn_main_menu_1': 'Назад в меню',

    'video_bild1': 'BAACAgIAAxkBAAIeh2W5amSK8tqxgH9WqRlAueFJt4LzAALJQAACsSnISerQUfo1RqT7NAQ',
    'video_bild2': 'BAACAgIAAxkBAAIeimW5bX_Eqds5L3BBaTdEqOVaRYxIAALPQAACsSnISRhttNal6aLVNAQ',
    'video_bild3': 'BAACAgIAAxkBAAIfE2W6qPiJMelSvj5gPG4qcOXXpMKbAAJYQwACsSnQSddu_DcdKx8jNAQ',
    'video_bild4': 'BAACAgIAAxkBAAIfFmW6qWlqn07d1ksLOJUC8WIWQz4ZAAJaQwACsSnQSRPUlFGMsjCcNAQ',
    'video_bild_info1': 'ОАО “Радошковичский керамический завод”.',
    'video_bild_info2': 'ООО "Арена Ритейл"',
    'video_bild_info3': 'ООО «Анексартисиас»',
    'video_bild_info4': 'ООО «Анексартисиас»',

    'video_elect1': 'BAACAgIAAxkBAAIfJWW6r9bQGoqx3azZ9urW4bE8pbhKAALdOgACsSnYSXRE8JlCWHaoNAQ',
    'video_elect2': 'BAACAgIAAxkBAAIfJmW6r9Yjya6nLxyErqJzq7_wJvagAALPRgACrhnASXrWSwLx_dpNNAQ',
    'video_elect_info1': 'ООО «МакСолюшнс».Breezy.',
    'video_elect_info2': 'Ноутбук HORIZONT H-BOOK PRO.',

    'video_car1': 'BAACAgIAAxkBAAIfNWW6su6p_dc5Lk1b8IBsdfJS_zMyAAIBOwACsSnYSS2cWpoJZtIJNAQ',
    'video_car2': 'BAACAgIAAxkBAAIfMmW6sEtzpSKYrkCOGSI0nwPjzBffAALfOgACsSnYSd6EJm-NDzN2NAQ',
    'video_car3': 'BAACAgIAAxkBAAIfJ2W6r9bEYMH5BEH7FU4lTm0qnmAVAALRRgACrhnASdGGu2r80887NAQ',
    'video_car_info1': 'GSM GRAND SEVEN MOTORS.',
    'video_car_info2': 'EV-PANDA. Электрические автомобили.',
    'video_car_info3': 'Доставка авто. WESTMOTORS.',

    'video_food1': 'BAACAgIAAxkBAAIf9WW78L3VfMR2WAOF-31l2Wz1QCyzAALDRQACfkrhScDS277ZTvYzNAQ',
    'video_food2': 'BAACAgIAAxkBAAIf-GW78TUHuYwJmrLHqimWH7ErpPUvAALHRQACfkrhSVUnYLR5uIVdNAQ',
    'video_food_info1': 'Обзор суши. Корпоратив Сливки Бай.',
    'video_food_info2': 'Panzarotti. Галерея Минск.',
}

LEXICON_PRICE: dict[str, str] = {
    'photo_telega': 'Следующее фото',
    'btn_main_menu_1': 'Назад в меню',
    'manager': 'Менедж🤓р',
    'photo_telejka1': 'AgACAgIAAxkBAAIVnWV_WWmU1Ul6igGnYCW8xkgF2B2kAAJl1DEbenr5S1NmyoDaJlKbAQADAgADcwADMwQ',
    'photo_tekejka2': 'AgACAgIAAxkBAAIP32VQxP_m8psGQI4jDsHz_ORUjZrLAAIa0zEbASOISqKwIV5RRk0UAQADAgADcwADMwQ',
    'telejka_info': '<b>Пост в телеграм канале Скидки Беларуси.</b>\n'
                    '✅Количество подписчиков - 46 000.\n'
                    '✅Количество просмотров - более 10 000.\n\n'
                    '💵1 выход - 798 руб.\n'
                    '<a href="https://t.me/slivki_by">Ссылка на telegram</a>\n',

    'first_photo': "AgACAgIAAxkBAAIQLGVRE7NaXH5M8hyJOWivDtaFwtLfAAJt1TEbASOISq_5Ki2Jo-B-AQADAgADcwADMwQ",
    'first_photo_info': '❗36 000+ уникальных пользователей в день.\n'
                        '❗11 000+ компаний партнеров за все время.\n'
                        '❗695 000+ уникальных пользователей в месяц.\n'
                        '<a href="https://www.slivki.by/">Ссылка на сайт</a>\n',

    'photo_podlojka1': 'AgACAgIAAxkBAAIPl2VQtCR3g09DCIWgL7D54jfWKBliAAKr0jEbASOISm8yc_xSXArCAQADAgADcwADMwQ',
    'photo_podlojka2': 'AgACAgIAAxkBAAIPpmVQvjGBaaIV0tK2tcGbA5gbMDDcAALf0jEbASOISjMSXEYm9pcpAQADAgADcwADMwQ',
    'photo_podlojka3': 'AgACAgIAAxkBAAIPsWVQwqpw_L4TVzQbPwKQW_YeOS82AAL-0jEbASOISvTZc0JabhnDAQADAgADcwADMwQ',
    'podlojka_info': '<b>Брендированная подложка.</b> Дублируется в мобильной версии сайта.\n'
                     '✅CTR - 0.17%|CPM-1.65 руб.\n'
                     '✅Показы за месяц - 2 019 398\n'
                     '✅Клики - 3 265 \n',
    'podlojka_info2': '<b>Брендированная подложка.</b>\n'
                      '💵Сутки - 185 руб.\n'
                      '💵Месяц - 2998 руб. (Минск).\n'
                      '💵Месяц - 4998 руб. (Вся РБ).\n',

    'banner_top1': 'AgACAgIAAxkBAAIQFGVQ0of13KyvXndrViwecRvjiGlEAAKH0zEbASOISiQcEQUCp4AJAQADAgADcwADMwQ',
    'banner_top2': 'AgACAgIAAxkBAAIQF2VQ0pc2pkinizdODAxtvkcmjRirAAKK0zEbASOISrEZFt2zJEhbAQADAgADcwADMwQ',
    'banner_top3': 'AgACAgIAAxkBAAIQGmVQ0xUfZxrZGdriO86FAgy7HzKIAAKN0zEbASOISm85YYm4LDiHAQADAgADcwADMwQ',
    'banner_top_info': '<b>Баннерная растяжка.</b> Дублируется в мобильной версии сайта.\n'
                       '✅CTR-0.10%|CPM-1.37 руб.\n'
                       '✅Показы за месяц - 3 533 947\n'
                       '✅Клики - 3082 \n',
    'banner_top_info2': '<b>Баннерная растяжка.</b>\n'
                        '💵Сутки - 128 руб.\n'
                        '💵Месяц - 2498 руб. (Минск).\n'
                        '💵Месяц - 3998 руб.(Вся РБ).\n',

    'brendbox1': 'AgACAgIAAxkBAAIQM2VRGqTHOM8jNGyon6TOSSOU-9gFAAKT1TEbASOISuk9W6J0X8YlAQADAgADcwADMwQ',
    'brendbox2': 'AgACAgIAAxkBAAIQNmVRGrs8yBvCo4I5egwKhaL3UWR2AAKU1TEbASOISr2ihzV3mYajAQADAgADcwADMwQ',
    'brendbox3': 'AgACAgIAAxkBAAIQOWVRGuR65-cYZWRS17FPXHL0JJYCAAKV1TEbASOISp5gVUsw-QhJAQADAgADcwADMwQ',
    'brendbox_info': '<b>БРЕНДБОКС в "ХИТАХ"</b>.\n'
                     'С закреплением на главной странице в рубрике "ХИТЫ".\n'
                     'Высокая посещаемость рубрики. Дублируется в мобильной версии.',
    'brendbox_info2': '<b>БРЕНДБОКС в "ХИТАХ".</b>\n'
                      '✅CTR-0.27%|CPM-4.88 руб.\n'
                      '✅Показы - 255 080\n'
                      '✅Клики - 1 154\n'
                      'В некоторых тематиках можно получить больше кликов.',
    'brendbox_info3': '<b>БРЕНДБОКС в "ХИТАХ"</b>.\n'
                      '💵Месяц(1-6 место) - 1 698 руб.\n'
                      '💵Месяц(7-9 место) - 1 498 руб.\n',

    'brendbox_heading1': 'AgACAgIAAxkBAAIQWGVRRYO_eBV93zi4pqUOEMKWaL19AAK_0jEbASOQSu8x9TK1p0VsAQADAgADcwADMwQ',
    'brendbox_heading2': 'AgACAgIAAxkBAAIQW2VRRZuFlAwhWPT_gwhr2hB1FyRJAALA0jEbASOQSqKsk63tL3uSAQADAgADcwADMwQ',
    'brendbox_heading_info': '<b>БРЕНДБОКС в рубрике.</b>\n'
                             'Размещается в тематической рубрике.\n'
                             'Дублируется в мобилной версии сайта.\n'
                             '✅CTR-2.31%|CPM-1.58 руб.\n'
                             '💵Месяц - 498 руб.\n',
    'brendbox_heading_info2': '<b>БРЕНДБОКС в рубрике "НОВОЕ"</b>.\n'
                              '💵Месяц(1-2 строка) - 697.8 руб.\n'
                              '💵Месяц(4 строка) - 598.8 руб.\n'
                              '💵Месяц(6 строка) - 398.7 руб.\n',
    'floating1': 'AgACAgIAAxkBAAIQiGVSkUuU_oMrgDXQktkgnXvvHQxzAAKp2TEbXRyYSrn33fUyc9VPAQADAgADcwADMwQ',
    'floating2': 'AgACAgIAAxkBAAIQi2VSkVZS1aqeN1rFU4hWlPudhR3UAAJ9yTEbZuyZSiNoN7u5SHzLAQADAgADcwADMwQ',
    'floating_info': '<b>ФЛОАТИНГ</b>.\n'
                     'Размещается только в мобильной версии.\n'
                     'В рубрике размещается в нижней части экрана, а в акции - в верхней, чтобы не закрывать кнопки.',
    'floating_info2': '<b>ФЛОАТИНГ</b>.\n'
                      '✅CTR-1.06%|CPM-1.84 руб.\n'
                      '✅Показы за месяц - 2 587 677\n'
                      '✅Клики - 27 582 \n'
                      '💵Месяц(скозная) - 1998 руб.\n'
                      '💵Месяц(в рубрике) - 998 руб.\n',

    'banner_horizontal1': 'AgACAgIAAxkBAAIQbWVScI1OZitVCuewX21PMvCBQX7yAAJZ0TEbZuyRSg6I13ULnYNFAQADAgADcwADMwQ',
    'banner_horizontal2': 'AgACAgIAAxkBAAIQcGVScJs3olzIAAGA5ax5u9zME3IlFgACWtExG2bskUpCcIy4Zuu21QEAAwIAA3MAAzME',
    'banner_horizontal_info': '<b>Баннер горизонтальный в рурике "ХИТЫ"</b>.\n'
                              'Дублируется в мобильной версии.\n'
                              'Размещается и на главной странице.',
    'banner_horizontal_info2': '<b>Баннер горизонтальный в рурике "ХИТЫ"</b>.\n'
                               '✅CTR-0.06%|CPM-1.72 руб.\n'
                               '💵Месяц - 598 руб.\n',

    'advertising_news1': 'AgACAgIAAxkBAAIQemVSf1X9EKb27lzy2TWbB-XhNC5HAAI9yTEbZuyZStOWwz2yTrd_AQADAgADcwADMwQ',
    'advertising_news2': 'AgACAgIAAxkBAAIQfWVSf2N4un2itqtBTqV34oPxgm2UAAI-yTEbZuyZStdHqavVr_JyAQADAgADcwADMwQ',
    'advertising_news_info': '<b>Рекламная новость. Новость дня</b>.\n'
                             'Отображается только на главной странице.\n'
                             'Дублируется в мобильной версии.\n'
                             '✅CTR-0.11%|CPM-1.84 руб.\n',
    'advertising_news_info2': '<b>Рекламная новость. Новость дня.</b>\n'
                              '1 выход -1 сутки.\n'
                              '💵1 выход - 199 руб.\n'
                              '💵2 выхода - 258 руб.\n'
                              '💵4 выхода - 376 руб.\n'
                              '💵6 выхода - 494 руб.\n',

    'brendbox_premium1': 'AgACAgIAAxkBAAIQqWVT1LIZ-JzIik4esjFoJGWKVty7AALi1TEbXRygSmCmslUW4-xTAQADAgADcwADMwQ',
    'brendbox_premium2': 'AgACAgIAAxkBAAIQrGVT1L9eRLoWwq1RTiI-nhClPpb2AALj1TEbXRygSuJGO8dVuYr8AQADAgADcwADMwQ',
    'brendbox_premium_info': '<b>Премиум брендбукс/Сайдбар.</b>\n'
                             'Размещается только в десктопной версии.\n'
                             'Есть возможность размещения видео-баннера.\n',
    'brendbox_premium_info2': '<b>Премиум брендбукс/Сайдбар.</b>\n'
                              '✅CTR-0.08%|CPM-1.14 руб.\n'
                              '✅Показы за сутки - 272 356\n'
                              '✅Клики - 356 \n'
                              '💵1 выход(сутки) - 298.8 руб.\n',

    'insta1': 'AgACAgIAAxkBAAIQ1WVWhjGiSKtpPl5QB-tJCZdhHmhcAAK_2zEbE0WwSk3G9r6HZcM3AQADAgADcwADMwQ',
    'insta2': 'AgACAgIAAxkBAAIQt2VT4PXNV8swE6hshpoBZygsA382AAL61TEbXRygSs9x72PnKdXQAQADAgADcwADMwQ',
    'insta3': 'AgACAgIAAxkBAAIRLGVabutt69opnMcQ0z4tKaCkQr9VAAKN1TEbZcDYSi7nus28iFYLAQADAgADcwADMwQ',
    'insta4': 'AgACAgIAAxkBAAIRM2VadUK9MsygaEfPIy56_owUt6HTAAKa1TEbZcDYSuC17cOQUAVWAQADAgADcwADMwQ',
    'insta5': 'AgACAgIAAxkBAAIRNmVafLrGJ4BL8o48Uy0clV2vNn7-AAJX1jEbZcDYSpNKR9P0_Z3-AQADAgADcwADMwQ',
    'insta6': 'AgACAgIAAxkBAAIRT2Vbwy6w8OhApKfWyGcPmfvBwbFbAAJszDEb6HnhSr0YfRvR0-Y-AQADAgADcwADMwQ',
    'insta7': 'AgACAgIAAxkBAAIRUmVbw02Grm3N2G-FDpATu_cKIAZiAAJtzDEb6HnhStEXMYOLJMKeAQADAgADcwADMwQ',
    'insta8': 'AgACAgIAAxkBAAIRWWVb0HjKeGs8Kg_XbgqVn5ECtKF9AAKNzDEb6HnhSpTHZpoVcZ_IAQADAgADcwADMwQ',
    'insta9': 'AgACAgIAAxkBAAIRXGVb0IZAW-snulYaULd50cbEKNAYAAKOzDEb6HnhSjPMCwOiroN-AQADAgADcwADMwQ',
    'insta10': 'AgACAgIAAxkBAAIRlmVc_hV3UpSl7yM61mK2Xwp273sMAAL21DEbWbjoSjytK9W4C3NSAQADAgADcwADMwQ',
    'insta_info': '<b>Cеть инстаграм Сливки бай.</b>\n'
                  '✅Больше 700 000 подписчиков.\n'
                  '✅30 блогеров в штате.\n'
                  '✅15 Instagram-каналов в РБ.\n',
    'insta_info2': '<b>Cеть инстаграм Сливки бай.</b>\n'
                   '✅250 000+ пользователей смотрят Reels-видео.\n'
                   '✅275 000+ недельный охват пользователей.\n'
                   '✅200 000+ охват поста.\n'
                   '✅55 000+ просмотров видеоистории в сутки.\n'
                   '✅15 000+ кликов по ссылке в сторис.\n',
    'insta_info3': '<b>Cеть инстаграм Сливки бай.</b>\n'
                   '✅3 основных канала:\n'
                   'Канал - slivkiby (365 000 подписчиков).\n'
                   'Канал giperspros (108 000 подписчиков).\n'
                   'Канал slivkiby_beauty (23 300 подписчиков).\n'
                   '✅12 региональных каналов.\n'
                   'Все каналы /insta_links',
    'insta_info4': '<b>Основной канал slivkiby.</b>\n'
                   '✅365 000 подписчиков.\n'
                   '✅200 000+ охват поста в ленте.\n'
                   '✅55 000+ просмотров видеоистории в сутки.\n'
                   '<a href="https://www.instagram.com/slivkiby/">www.instagram.com/slivkiby/</a>\n',
    'insta_info5': '<b>Основной канал slivkiby.</b>\n'
                   'Стоимость размещения:\n'
                   '💵Видеообзор(сторис 24 ч.) - 1698 руб.\n'
                   '💵Пост(рилс) - 2998 руб.\n'
                   '💵Пост + Видеообзр - 3998 руб.\n'
                   '💵Одностраничный сторис(1 выход) - 498 руб.\n',
    'insta_info6': '<b>Канал giperspros.</b>\n'
                   '✅108 000 подписчиков.\n'
                   '✅70 000+ охват поста в ленте.\n'
                   '✅40 000+ просмотров видеоистории в сутки.\n'
                   '<a href="https://www.instagram.com/giperspros/">www.instagram.com/giperspros/</a>\n',
    'insta_info7': '<b>Канал giperspros.</b>\n'
                   'Стоимость размещения:\n'
                   '💵Видеообзор(сторис 24 ч.) - 798 руб.\n'
                   '💵Пост(рилс) - 998 руб.\n'
                   '💵Пост + Видеообзр - 1498 руб.\n'
                   '💵Одностраничный сторис(1 выход) - 298 руб.\n',
    'insta_info8': '<b>Канал slivkiby_beauty.</b>\n'
                   '✅24 000 подписчиков.\n'
                   '✅30 000+ охват поста в ленте.\n'
                   '✅20 000+ просмотров видеоистории в сутки.\n'
                   '<a href="https://www.instagram.com/slivkiby_beauty/">www.instagram.com/slivkiby_beauty/</a>\n',
    'insta_info9': '<b>Канал slivkiby_beauty.</b>\n'
                   'Стоимость размещения:\n'
                   '💵Видеообзор(сторис 24 ч.) - 798 руб.\n'
                   '💵Пост(рилс) - 998 руб.\n'
                   '💵Пост + Видеообзр - 1498 руб.\n'
                   '💵Одностраничный сторис(1 выход) - 298 руб.\n',
    'insta_info10': '<b>Розыгрыши в Instagram.</b>\n'
                    'В любом из каналов могут быть проведены розыгрыши.\n'
                    '💵 Стоимость розыгрыша - стомость поста или обзора + 300 - 500 рублей.\n',

    'app1': 'AgACAgIAAxkBAAISp2VpCVq0BXej7OZ6VOAQkgT8isRgAAJI0zEbkHVRS6s3Krc9F98nAQADAgADcwADMwQ',
    'app2': 'AgACAgIAAxkBAAISpGVpCTMDUWSRcg6266wiuRhHZ-fZAAJH0zEbkHVRS_T4gh9T9h4SAQADAgADcwADMwQ',
    'app3': 'AgACAgIAAxkBAAISqmVpCX0q5T3UoPuPIbvV_CSmMoMVAAJJ0zEbkHVRS2aPaKb4pNdiAQADAgADcwADMwQ',
    'app4': 'AgACAgIAAxkBAAISrWVpCZ6TZE8LMMWHGuCveXXGlwddAAJK0zEbkHVRS_wotV6tk1n-AQADAgADcwADMwQ',
    'app_info1': '<b>Преимущества приложения SLIVKI:</b>\n'
                 '✅Быстрая регистрация по номеру телефона.\n'
                 '✅Поддержка работы даже на старых версиях ОС.\n'
                 '✅Поиск акций поблизости (при включенной геолокации).\n'
                 '✅Возможность добавлять понравившиеся акции в «Избранное».\n',
    'app_info2': '<b>Бренд-старт в мобильном прилжении.</b>\n'
                 '✅Размещается только в мобильном прилжении.\n'
                 '✅Появляется при первом заходе в приложение.\n'
                 '✅Материл и ссылку можно менять.\n'
                 '✅Показы - 563 573, клики - 6 572.\n'
                 '✅CTR - 0.17%|CPM-1.65 руб.\n',
    'app_info3': '<b>Бренд-старт в мобильном приложении.</b>\n'
                 '💵Минск. 10 суток - 1498 руб.\n'
                 '💵Минск. 30 суток - 3998 руб.\n'
                 '💵Регион (столица + 3-5 городов). 30 суток - 998 руб.\n'
                 '💵РБ (6 столиц + 20 городов). 30 суток - 5998 руб.\n'
                 '💵Производство ролика - 998 руб. '
                 'Либо бесплатно, при его создании в Instagram.\n',
    'app_info4': '<b>Сторис в приложении.</b>\n'
                 '💵1 сутки - 498 руб.\n'
                 '💵5 суток - 798 руб.\n'
                 '💵10 суток - 1298 руб.\n'
                 '💵Производство ролика - 998 руб. '
                 'Либо бесплатно, при его создании в Instagram.\n'
                 '✅Ссылка ведет на нужную страницу.\n\n'
                 '<a href="https://www.slivki.by/prilozhenie-skidok">Скачать приложение</a>\n',

    'bloger1': 'AgACAgIAAxkBAAIc_2W1dZqOJ4j7wAp6GcryvM04D_opAAI-2jEb9EyxSaSh1idlup65AQADAgADcwADNAQ',
    'bloger2': 'AgACAgIAAxkBAAIdC2W1gKImroT9Qcl64keS1S9vkdZzAAJj2jEb9EyxSWjWsb88FnHzAQADAgADcwADNAQ',
    'bloger3': 'AgACAgIAAxkBAAIc_GW1dYmfEI2VwMCUonHYs0ZsypfDAAI82jEb9EyxSQr-lJzx9p7LAQADAgADcwADNAQ',
    'bloger4': 'AgACAgIAAxkBAAIdAmW1db20yKg15A5ZxoMWMzhy0bl_AAJA2jEb9EyxSRpABMDIEhbsAQADAgADcwADNAQ',
    'bloger5': 'AgACAgIAAxkBAAIdEWW1gOcXZIE35j0ZrC1dTsa2NCLqAAJl2jEb9EyxSe6e5qlYLkF0AQADAgADcwADNAQ',
    'bloger6': 'AgACAgIAAxkBAAIdFGW1gQZmw0G54HlEigOqzqUHR_DhAAJm2jEb9EyxSb_vgKggnXiLAQADAgADcwADNAQ',
    'bloger7': 'AgACAgIAAxkBAAIdCGW1gJGcHAUo8Cvp6erFoON8N5cHAAJi2jEb9EyxSQmAtO6p76ZhAQADAgADcwADNAQ',
    'bloger8': 'AgACAgIAAxkBAAIdBWW1gEn0Uz5hRzMoLinmmu8C6JG7AAJg2jEb9EyxSWrqhWr9c9qsAQADAgADcwADNAQ',
    'bloger9': 'AgACAgIAAxkBAAIdDmW1gNKr4XGQyoxlLyQ3JVLVdwbkAAJk2jEb9EyxSfLXDRFbUX_jAQADAgADcwADNAQ',
    'bloger_info1': '<a href="https://www.instagram.com/diana.blaga/">Инстаграм Дианы.</a>\n',
    'bloger_info2': '<a href="https://www.instagram.com/v_vitkovskiy/">Инстаграм Вадима.</a>\n',
    'bloger_info3': '<a href="https://www.instagram.com/katrin_logunova/">Инстаграм Кати.</a>\n',
    'bloger_info4': '<a href="https://www.instagram.com/_tamilaya/">Инстаграм Тамилы.</a>\n',
    'bloger_info5': '<a href="https://www.instagram.com/kirrpetrov/">Инстаграм Кирила.</a>\n',
    'bloger_info6': '<a href="https://www.instagram.com/foolovskiy/">Инстаграм Алексея.</a>\n',
    'bloger_info7': '<a href="https://www.instagram.com/yanapytko/">Инстаграм Яны.</a>\n',
    'bloger_info8': '<a href="https://www.instagram.com/pisaryk26/">Инстаграм Анны.</a>\n',
    'bloger_info9': '<a href="https://www.instagram.com/schamaluk/">Инстаграм Кости.</a>\n',

    'tiktok1': '<b>TIK-TOK SLIVKI.</b>\n'
               '✅170 000 подписчиков.\n'
               '✅11 каналов.\n'
               '✅До 1 000 000 и выше просмотров роликов.\n\n'
               '<b>Стоимость размещения:</b>\n'
               '💵Публикация (не лезть в сценарий) Минск. 1 выход - 498 руб.\n'
               '💵В пакете с инстаграмом. Минск. 1 выход - 298 руб.\n'
               '💵Пост инста, сторис интса, тикток. По 1 выходу - 3898 руб.\n'
               '💵Пост + сторис в Минске, тикток, телеграм. По 1 выходу - 4398 руб.\n',
    'tiktok2': '<b>TIK-TOK SLIVKI.</b>\n'
               '<b>Стоимость размещения:</b>\n'
               '💵Минск. 1 выход - 998 руб.\n'
               '💵Минск и 3 любых города.  По 1 выходу - 998 руб.\n'
               '💵Минск + 5 лучших городов.  По 1 выходу - 1498 руб.\n'
               '💵Любой город в отдельности.  1 выход - 398 руб.\n'
               '💵3 любых города без Минска.  По 1 выходу - 898 руб.\n'
               '💵10 городов.  По 1 выходу - 1998 руб.\n\n'
               'Все каналы /tiktok_links\n',

}

LEXICON_btn_faq: dict[str, str] = {
    'main_menu': 'Назад в меню',
    'faq_1': 'Как начать сотрудничество?',
    'faq_1_info': '<b>Как начать сотрудничество?</b>\n'
                  '✅Свяжитесь со специалистом по продажам.\n'
                  '✅Совместо со специалистом по продажам определите вид размещения, который подходит вам.\n'
                  '✅Оплатите счет.\n'
                  '✅Разместите рекламу.',
    'faq_2': 'Сколько стоит размещение?',
    'faq_2_info': '<b>Сколько стоит размещение?</b>\n'
                  'Есть базовый прайс, опираясь на который можно получить информацию о стоимости.'
                  ' При формировании конечного предлоения учитывается:\n'
                  '✅Объем планируемых активностей.\n'
                  '✅История отношений между нами.\n'
                  '✅Перспектива сотрудничества.\n'
                  '✅Тематика сотрудничества.\n',
    'faq_4': 'Способы оплаты.',
    'faq_4_info': '<b>Способы оплаты.</b>\n'
                  'Код 22601 Реклама. «Платежи за оказание услуг по производству, размещению, распространению рекламы»\n\n'
                  'Клиент может оплатить:\n'
                  '✅С рачетного счета компании клиента.\n'
                  '✅Через кассу в любом банке/почте. '
                  'Предоставить счет на оплату от нашей компании кассиру. '
                  'Обязательно сообщить "за рекламу, <b>не через систему ерип</b>".\n'
                  'Прислать фото документа, подтвежадющего оплату.\n'
                  '✅Банковской картой через личный кабинет. Переводы - юридическому лицу - по реквизитам - произвольный платеж.\n'
                  'Зависит от прилжения конкретного банка.\n'
                  'Из счета для оплаты внесите наши реквизиты. Назначение платежа - "не в бюджет за рекламу".\n'
                  'Прислать фото документа, подтвежадющего оплату.',
    'faq_3': 'У вас дорого.',
    'faq_3_info': '<b>У вас дорого.</b>\n'
                  'У нас много вариантов размещения. Бюджеты могут быть от 45 рублей в месяд до 10 000 рублей и больше. '
                  'Для того, чтобы выбрать правильные рекламные инструменты и провести эффективную'
                  ' рекламную компанию, необходимо ответственно подойдти к поставленной задаче. Партнерский подход значительно '
                  'повысит шансы на успешный результат.',
    'faq_5': 'Информация для создани акции.\n',
    'faq_5_info':  '<b>Для запуска акции необходимо:</b>\n'
                   '✅Реквизиты. Указать директора и на основании чего он действует.\n'
                   '✅Логотип.\n'
                   '✅Маркетинговое название.\n'
                   '✅Ссылки на сайт и инсту.\n'
                   '✅Контактные телефоны, адрес эл. почты.\n'
                   '✅Адрес заведения.\n'
                   '✅График работы.\n'
                   '✅Фотографии заведения или места, где оказываются услуги.\n'
                   '✅Фотографии работ.\n'
                   '✅Фотографии мастеров с указанием опыта.\n'
                   '✅Видео материалы (желательно ссылки на инсту или ютуб.\n'
                   '✅Стоимость услуги до скидки и после скидки.\n'
                   '✅Преимущества компании.\n'
                   '✅Заполнить бриф.\n',

}
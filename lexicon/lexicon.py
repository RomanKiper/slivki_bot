LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'ГЛАВНОЕ МЕНЮ',
    '/admin': 'АДМИНКА',
    '/help': 'ПОМОЩЬ',
}

LEXICON_HI = {"привет", "здорова", "хай", "приветствую", "добрый день", "здравствуйте", "здрасти", "hi", "hello",
               "good morning", "good day"}

restricted_words = {'дурак', 'осел', 'болван', 'пидор', 'сидор', 'хуй'}


LEXICON_RU: dict[str, str] = {
    '/help': 'Тебе доступны команды:\n'
             '/start - запуск бота.\n'
             '/help - список команд.\n'
             '/description - описание бота.\n'
             '/insta_links - список ссылок на каналы instagram.\n'
             '/tiktok_links - список ссылок на каналы TikTok.\n'
             'Ты можешь воспользваться основным меню!\n'
             '👇👇👇 Меню.'
    ,
    '/admin+panel': '<b>Административная панель.</b>\nТы можешь добавить/изменить/удалить услуги, баннеры, КП, заметки и документы.'
    ,
    '/description_slivki':
        '<b>Сливки бай - это крупнейший маркетплэйс скидок в РБ.</b>\n'
        '✅13 лет на рынке услуг.\n'
        '✅1 000 000+ пользователей на сайте в месяц.\n'
        '✅1 000 000+ установок приложения.\n'
        '✅700 000+ подписчиков в социальных медиа.\n'
        '✅11 000+ партнеров.\n'
        '✅16 Instagram-каналов в РБ.\n'
        '✅30 блогеров в штате.\n'
        '✅40 городов в Беларуси.\n\n'
        '👨‍👨‍👧‍👦Аудитория Сливки Бай - активное население Беларуси со средним доходом и с яркой жизненной позицией.\n'
    ,

    '/office_adress':
        "Адрес:\nг. Минск, Проспект Независимости, 32А, строение 4\n"
        "БЦ 'Проспект' \n"
        "6 этаж\n",

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
                    '<a href="https://www.instagram.com/slivkiby_beauty/">www.instagram.com/slivkiby_beauty</a>\n'
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
                    '<a href="https://www.instagram.com/akcii_skidki_belarus/">www.instagram.com/akcii_skidki_belarus</a>\n'
    ,

    '/telega_links': '<b>Ссылки на каналы Telegram:</b>\n'
                    '<a href="https://t.me/slivki_by">https://t.me/slivki_by</a>\n'
                    '<a href="https://t.me/slivkiby_mogilev">https://t.me/slivkiby_mogilev</a>\n'
                    '<a href="https://t.me/slivkiby_gomel">https://t.me/slivkiby_gomel</a>\n'
                    '<a href="https://t.me/slivkiby_vitebsk">https://t.me/slivkiby_vitebsk</a>\n'
                    '<a href="https://t.me/slivkiby_bobruysk">https://t.me/slivkiby_bobruysk</a>\n'
                    '<a href="https://t.me/slivki_brest">https://t.me/slivki_brest</a>\n'
                    '<a href="https://t.me/slivki_baranovichi">https://t.me/slivki_baranovichi</a>\n'
                    '<a href="https://t.me/slivkiby_grodno">https://t.me/slivkiby_grodno</a>\n'
    ,

    '/agreement_links': '<b>Ссылки на договоры оферты:</b>\n'
                     '<a href="https://www.slivki.by/publichnyj-dogovor-okazaniya-reklamnyh-uslug-i-razmesheniya-akcij">Публичный договор возмездного оказания рекламных услуг</a>\n\n'
                     '<a href="https://www.slivki.by/dogovor-oferta-instagram">Договор оферта инстаграм</a>\n'

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
        "ЦЕНЫ/СТАТИСТИКА🤑💵": "price_statistic",
        "О НАС": "about",
        "FAQ🤯": "faq_main",
        "БЛОГЕРЫ👩‍🎤": "blogers-main",
        "ССЫЛКИ🔗": "links_main",
        "КОНТАКТЫ": "contacts_main",
        "ПРЕЗЕНТАЦИЯ🎁": "presentation_main",
    }

LEXICON_btn_help: dict[str, str] = {
        "Инструкция для админки📄": "adm_panel_instruction",
        "Связь с администратором📞": "adm_connect",
        "Общая информация🪬": "main_information",
    }


LEXICON_btn_main_links: dict[str, str] = {
        "САЙТ SLIVKI.BY": "site_slivki_link",
        "ИНСТАГРАМ ВСЕ": "insta_all_links",
        "ТИКТОК ВСЕ": "tiktok_all_links",
        "ТЕЛЕГРАМ ВСЕ": "telegram_all_links",
        "ДОГ-Р ОФЕРТЫ": "agreement_links",
        "ПРИЛОЖЕНИЕ": "app-link",
        "ТАБЛИЦЫ": "tables_links",
        "ПРАЙСЫ": "valable_prices_list",
        "ДОКУМЕНТЫ": "presentations_list",
        "ОПЕРАТИВНАЯ ИНФОРМАЦИЯ": "useful_information",
        "НАЗАД В МЕНЮ": "main_menu",
    }


LEXICON_btn_main_admin_menu: dict[str, str] = {
        "Создать услугу": "add_product",
        "Услуги": "products_list",
        "Создать КП": "add_offer",
        "Готовые КП": "offers_list",
        "Создать FAQ": "add_faq",
        "Список FAQ": "faq_list",
        "Создать заметку": "add_note",
        "Список заметок": "note_list",
        "Добавить прайс": "add_price",
        "Список прайсов": "price_list",
        "Добавить документ": "add_docoment",
        "Список документов": "documents_list",
        "Баннер.Добав/измен.": "add_change_banner",

    }

LEXICON_btn_add_offer: dict[str, str] = {
        "Next": "next_offer",
        "ADD": "add_to_offer",
        "Back": "previos_offer",
        "Смотреть КП": "products_in_offer",
        "Сохранить КП": "generate_offer",
    }


LEXICON_btn_employee_menu: dict[str, str] = {
    'tables_links': 'Рабочие таблицы',
    'work_links': 'Рабочие ссылки',
    'offer_online': 'Создать КП',
    'admin': 'Админка',
}

LEXICON_btn_price_statistic: dict[str, str] = {
        'САЙТ/РЕКЛАМА': 'site_slivki_advertising',
        'САЙТ/АКЦИЯ🔥': 'site_slivki_promotion',
        'INSTAGRAM': 'instagram_sl',
        'TELEGRAM': 'telegram_sl',
        'TIKTOK': 'tiktok_sl',
        'ПРИЛОЖЕНИЕ': 'app_advertising',
        'РЕГИОНЫ': 'regions_sl',
        'ОБЗОРЫ/ПРИМЕРЫ': 'reviews',
        'НАЗАД В МЕНЮ': 'main_menu',
    }

LEXICON_btn_back_to_main_menu: dict[str, str] = {
        'НАЗАД В МЕНЮ': 'main_menu',
    }

LEXICON_btn_back_to_advertising_menu: dict[str, str] = {
        'НАЗАД В МЕНЮ': 'price_statistic',
    }

LEXICON_btn_back_menu_links: dict[str, str] = {
        'НАЗАД В МЕНЮ': 'links_main',
    }

LEXICON_btn_slivki_site_link: dict[str, str] = {
        'slivki.by': 'https://www.slivki.by',
        'НАЗАД В МЕНЮ': 'links_main',
    }

LEXICON_btn_app_link: dict[str, str] = {
        'slivki.by': 'https://www.slivki.by/prilozhenie-skidok',
        'НАЗАД В МЕНЮ': 'links_main',
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
    'photo_telejka': 'AgACAgIAAxkBAAIqUmZiGnmOViRLmCcrRj-SuY9-j5cGAAI63DEbZGYRS466NWoZIJXqAQADAgADcwADNQQ',
    'telejka_info': '<b>Пост в телеграм канале Скидки Беларуси.</b>\n'
                    '✅Количество подписчиков - 46 000.\n'
                    '✅Количество просмотров - более 10 000.\n\n'
                    '💵1 выход - 798 руб.\n'
                    '<a href="https://t.me/slivki_by">Ссылка на telegram</a>\n',

    'first_photo': "AgACAgIAAxkBAAIqomZiKTMXRp9mxIu0YWulQdpx6e_DAAKq3DEbZGYRS9faoXCCx-_jAQADAgADcwADNQQ",
    'first_photo_info': '❗36 000+ уникальных пользователей в день.\n'
                        '❗11 000+ компаний партнеров за все время.\n'
                        '❗695 000+ уникальных пользователей в месяц.\n'
                        '<a href="https://www.slivki.by/">Ссылка на сайт</a>\n',
    'photo_podlojka': 'AgACAgIAAxkBAAIqpWZiKX5J1DfoQ2Dy3qsYSCpKmdOhAAKs3DEbZGYRS4KCL_vrDDwFAQADAgADcwADNQQ',
    'podlojka_info': '<b>Брендированная подложка.</b> Дублируется в мобильной версии сайта.\n'
                     '✅CTR - 0.17%|CPM-1.65 руб.\n'
                     '✅Показы за месяц - 2 019 398\n'
                     '✅Клики - 3 265 \n'
                     '💵Сутки - 185 руб.\n'
                     '💵Месяц - 2998 руб. (Минск).\n'
                     '💵Месяц - 4998 руб. (Вся РБ).\n',
    'banner_top': 'AgACAgIAAxkBAAIqqGZiKYpipFIu2LfLiOXs4gTqaqatAAJK2TEbLD0YSxZRKBICbS2dAQADAgADcwADNQQ',
    'banner_top_info': '<b>Баннерная растяжка.</b> Дублируется в мобильной версии сайта.\n'
                       '✅CTR-0.10%|CPM-1.37 руб.\n'
                       '✅Показы за месяц - 3 533 947\n'
                       '✅Клики - 3082 \n'
                       '💵Сутки - 128 руб.\n'
                       '💵Месяц - 2498 руб. (Минск).\n'
                       '💵Месяц - 3998 руб.(Вся РБ).\n',
    'brendbox': 'AgACAgIAAxkBAAIqq2ZiKeeG1THECsLrPQP32a_vOl4UAAJL2TEbLD0YS3TGJVJ5qYjMAQADAgADcwADNQQ',
    'brendbox_info': '<b>БРЕНДБОКС в "ХИТАХ"</b>.\n'
                     'С закреплением на главной странице в рубрике "ХИТЫ".\n'
                     'Высокая посещаемость рубрики. '
                     'Дублируется в мобильной версии.\n'
                     '✅CTR-0.27%|CPM-4.88 руб.\n'
                     '✅Показы - 255 080\n'
                     '✅Клики - 1 154\n'
                     '💵Месяц(1-6 место) - 1 698 руб.\n'
                     '💵Месяц(7-9 место) - 1 498 руб.\n',
    'brendbox_heading': 'AgACAgIAAxkBAAIqsWZiKm6Rq0M1z5HP4S9yCWRZcdeDAAJP2TEbLD0YS-82OaEZ7vLgAQADAgADcwADNQQ',
    'brendbox_heading_new': 'AgACAgIAAxkBAAIqrmZiKhRmUg07OoJl0eydFucXYDNjAAJM2TEbLD0YS49Dgbz__wtOAQADAgADcwADNQQ',
    'brendbox_heading_info': '<b>БРЕНДБОКС в рубрике.</b>\n'
                             'Размещается в тематической рубрике.\n'
                             'Дублируется в мобилной версии сайта.\n'
                             '✅CTR-2.31%|CPM-1.58 руб.\n'
                             '💵Месяц - 498 руб.\n',
    'brendbox_heading_info_new': '<b>БРЕНДБОКС в рубрике "НОВОЕ"</b>.\n'
                              '💵Месяц(1-2 строка) - 697.8 руб.\n'
                              '💵Месяц(4 строка) - 598.8 руб.\n'
                              '💵Месяц(6 строка) - 398.7 руб.\n',
    'floating': 'AgACAgIAAxkBAAIqtGZiKq8AAWCV456Bi1pVWLu65ALC8gACUNkxGyw9GEs7-2AvBUiEcAEAAwIAA3MAAzUE',
    'floating_info': '<b>ФЛОАТИНГ</b>.\n'
                     'Размещается только в мобильной версии.\n'
                     'В рубрике размещается в нижней части экрана, а в акции - в верхней, чтобы не закрывать кнопки.\n'
                      '✅CTR-1.06%|CPM-1.84 руб.\n'
                      '✅Показы за месяц - 2 587 677\n'
                      '✅Клики - 27 582 \n'
                      '💵Месяц(скозная) - 1998 руб.\n'
                      '💵Месяц(в рубрике) - 998 руб.\n',
    'banner_horizontal': 'AgACAgIAAxkBAAIqt2ZiKurfVEsinJA4pwUK92XKzSK-AAJR2TEbLD0YS25TzLCc2e6LAQADAgADcwADNQQ',
    'banner_horizontal_info': '<b>Баннер горизонтальный в рурике "ХИТЫ"</b>.\n'
                              'Дублируется в мобильной версии.\n'
                              'Размещается и на главной странице.\n'
                               '✅CTR-0.06%|CPM-1.72 руб.\n'
                               '💵Месяц - 598 руб.\n',
    'advertising_news': 'AgACAgIAAxkBAAIqumZiKximt4FxqE8gNhvquMekhMGlAAJS2TEbLD0YS07vyq11h5ThAQADAgADcwADNQQ',
    'advertising_news_info': '<b>Рекламная новость. Новость дня</b>.\n'
                             'Отображается только на главной странице.\n'
                             'Дублируется в мобильной версии.\n'
                             '✅CTR-0.11%|CPM-1.84 руб.\n'
                             '1 выход -1 сутки.\n'
                             '💵1 выход - 199 руб.\n'
                             '💵2 выхода - 258 руб.\n'
                             '💵4 выхода - 376 руб.\n'
                             '💵6 выхода - 494 руб.\n',
    'brendbox_premium': 'AgACAgIAAxkBAAIqvWZiK0kv5OdAgBu9W8KPpgvhd5CDAAJU2TEbLD0YSx2u5lMsGBDoAQADAgADcwADNQQ',
    'brendbox_premium_info': '<b>Премиум брендбукс/Сайдбар.</b>\n'
                             'Размещается только в десктопной версии.\n'
                             'Есть возможность размещения видео-баннера.\n'
                              '✅CTR-0.08%|CPM-1.14 руб.\n'
                              '✅Показы за сутки - 272 356\n'
                              '✅Клики - 356 \n'
                              '💵1 выход(сутки) - 298.8 руб.\n',

    'insta1': 'AgACAgIAAxkBAAIqcmZiHdySnMx0T4DMpKd_CUgKj3wTAAJG3DEbZGYRS2PtLPrBo8l3AQADAgADcwADNQQ',
    'insta2': 'AgACAgIAAxkBAAIqdWZiHgwkdsx-J4LBXyFxTDk7j2zPAAJH3DEbZGYRS8nzP9XL0BEqAQADAgADcwADNQQ',
    'insta3': 'AgACAgIAAxkBAAIqeGZiHhZ-q-krkck5XMUIkDCVWT5WAAJI3DEbZGYRS5a9HalMG2GNAQADAgADcwADNQQ',
    'insta4': 'AgACAgIAAxkBAAIqe2ZiHiAu_06FlENjHAclICaIwrE_AAJJ3DEbZGYRSy-WDZvncz0KAQADAgADcwADNQQ',
    'insta5': 'AgACAgIAAxkBAAIqfmZiHipUsdXmRM-SCVu0erWug0FLAAJL3DEbZGYRS5GanEt3ykRJAQADAgADcwADNQQ',
    'insta_info1': '<b>Cеть инстаграм Сливки бай:</b>\n'
                  '✅Больше 700 000 подписчиков.\n'
                  '✅30 блогеров в штате.\n'
                  '✅15 Instagram-каналов в РБ.\n'
                  '✅250 000+ пользователей смотрят Reels-видео.\n'
                  '✅55 000+ просмотров видеоистории в сутки.\n'
                  '✅3 основных канала:\n'
                  'Канал - slivkiby (375 000 подписчиков).\n'
                  'Канал giperspros (108 000 подписчиков).\n'
                  'Канал slivkiby_beauty (23 300 подписчиков).\n'
                  '✅11 региональных каналов.\n'
                  'Все каналы /insta_links',
    'insta_info2': '<b>Основной канал slivkiby.</b>\n'
                   '✅375 000 подписчиков.\n'
                   '✅200 000+ охват поста в ленте.\n'
                   '✅55 000+ просмотров видеоистории в сутки.\n'
                   '<a href="https://www.instagram.com/slivkiby/">www.instagram.com/slivkiby/</a>\n'
                   'Стоимость размещения:\n'
                   '💵Видеообзор(сторис 24 ч.) - 1698 руб.\n'
                   '💵Пост(рилс) - 2998 руб.\n'
                   '💵Пост + Видеообзор - 3998 руб.\n',
    'insta_info3': '<b>Канал giperspros.</b>\n'
                   '✅108 000 подписчиков.\n'
                   '✅70 000+ охват поста в ленте.\n'
                   '✅40 000+ просмотров видеоистории в сутки.\n'
                   '<a href="https://www.instagram.com/giperspros/">www.instagram.com/giperspros/</a>\n'
                   'Стоимость размещения:\n'
                   '💵Видеообзор(сторис 24 ч.) - 798 руб.\n'
                   '💵Пост(рилс) - 998 руб.\n'
                   '💵Пост + Видеообзор - 1498 руб.\n',
    'insta_info4': '<b>Канал slivkiby_beauty.</b>\n'
                   '✅24 000 подписчиков.\n'
                   '✅30 000+ охват поста в ленте.\n'
                   '✅20 000+ просмотров видеоистории в сутки.\n'
                   '<a href="https://www.instagram.com/slivkiby_beauty/">www.instagram.com/slivkiby_beauty/</a>\n'
                   'Стоимость размещения:\n'
                   '💵Видеообзор(сторис 24 ч.) - 398 руб.\n'
                   '💵Пост(рилс) - 598 руб.\n'
                   '💵Пост + Видеообзор - 798 руб.\n',
    'insta_info5': '<b>Розыгрыши в Instagram.</b>\n'
                    'В любом из каналов могут быть проведены розыгрыши.\n'
                    'В зависимости от тематики, условий розыгрыша, ценности приза, количество '
                   'новых подписчиков в канале клиента от 1000 до 10000 и более.\n'
                    '💵 Стоимость розыгрыша - стомость поста или обзора + 300 - 500 рублей.\n',

    'app1': 'AgACAgIAAxkBAAIqX2ZiG6yEOXpRmrLpx64xYWl28AXyAAJA3DEbZGYRS0ci6w0tUI7bAQADAgADcwADNQQ',
    'app2': 'AgACAgIAAxkBAAIqYmZiG7rc6N04ioZFhw-uPIrd8Lf_AAJB3DEbZGYRS59nU-Ik58J6AQADAgADcwADNQQ',
    'app3': 'AgACAgIAAxkBAAIqZWZiG8ZtnUqhQzcgLAdnDzHQagH1AAJC3DEbZGYRS26iAiZcaisPAQADAgADcwADNQQ',
    'app4': 'AgACAgIAAxkBAAIqaGZiG9ISdb6Df_eGppqByKIff1tVAAJD3DEbZGYRSzokJZYfqZxeAQADAgADcwADNQQ',
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

    'region_page1': '<b>Реклама на сайте Сливки бай в региональных городах.</b>\n\n'
               '<b>Стоимость размещения 1-й акции с промокодом в любой рубрике:</b>\n'
               '💵 1 месяц - 39руб.\n'
               '💵 3 месяца - 69 руб.\n'
               '💵 6 месяц - 99 руб.\n'
               '💵 12 месяц - 149 руб.\n\n'
               '<b>Лазерная эпиляция/Аппаратное удаление волос:</b>\n'
               '💵 Новые компании. Первые 3 мес. - 49руб.\n'
               'Работающие компании:\n'
               '💵 1 месяц - 39 руб.\n'
               '💵 3 месяца - 250 руб.\n'
               '💵 6 месяц - 399 руб.\n'
               '💵 12 месяц - 699  руб.\n\n',
    'region_page2': '<b>Брендированная подложка (до 5 шт в ротации).</b>\n'
                    'Сквозная в одном из регионов. (Могилев, Гомель, Витебск, Гродно, Брест).\n'
                    '💵 1 месяц - 398 руб.\n\n'
                    '<b>Растяжка (до 5 шт в ротации).</b>\n'
                    'Сквозная в одном из регионов. (Могилев, Гомель, Витебск, Гродно, Брест).\n'
                    '💵 1 месяц - 398 руб.\n\n'
                    '<b>Мобильный флоатинг (5 шт в ротации).</b>\n'
                    'Сквозной. (на главной странице, в поиске сайта, в каждой рубрике).\n'
                    '💵 1 месяц - 250 руб.\n',
    'region_page3': '<b>Баннер горизонтальный.</b>\n'
                    'Десктоп/мобильная версия. 1 место.\n'
                    '💵 1 месяц - 149 руб.\n\n'
                    '<b>Закрепление акции (ТОП).</b>\n'
                    'В рубрике или поисковой выдаче сайта. На выбор.\n'
                    '💵 1 месяц - 50 руб.\n\n'
                    '<b>Закрепление акции (ТОП).</b>\n'
                    'В рубрике + поисковой выдаче сайта.\n'
                    '💵 1 месяц - 85 руб.\n',
    'region_page4': '<b>Региональные каналы instagram.</b>\n\n'
                    '<b>Instagram БРЕСТ.</b>\n'                   
                   '💵Видеообзор(сторис 24 ч.) - 398 руб.\n'
                   '💵Пост(рилс) - 498 руб.\n'
                   '💵Пост + Видеообзор - 788 руб.\n\n'
                   '<b>Instagram МОГИЛЕВ/ГОМЕЛЬ/ГРОДНО.</b>\n'                   
                   '💵Видеообзор - 300 руб.\n'
                   '💵Пост(рилс) - 498 руб.\n'
                   '💵Пост + Видеообзор - 688 руб.\n\n'
                   '<b>Instagram ВИТЕБСК/СВЕТЛОГОРСК/ПИНСК/БОБРУЙСК/ОРША/БАРАНОВИЧИ/БОРИСОВ.</b>\n'                   
                   '💵Видеообзор - 198 руб.\n'
                   '💵Пост(рилс) - 298 руб.\n'
                   '💵Пост + Видеообзор - 398 руб.\n\n'
                   'Все каналы /insta_links'
}


LEXICON_PROMOCOD_INFO: dict[str, str] = {
    'page_action1': '<b>Акция с промокодом — главный формат на сайте Cливки бай.</b>\n'
                    'Акция на сайте — это уникальное предложение '
                    'исключительно для пользователей нашего маркет-плейса. '
                    'Цена со скидкой по акции доступна только обладателю промокода. '
                    'Промокод — это гарантия цены со скидкой. '
                    'Потребитель обязан предоставить промокод с сайта Сливки бай, чтобы получить услугу/товар с уникальной скидкой. '
                    'Все остальные клиенты покупают по полной цене или по внутренней акции партнера, '
                    'где итоговая цена должна быть на 15% выше, чем по промокоду.',
    'page_action2': '<b>Как работает акция?.</b>\n'
                    '✅Наш пользователь видит акцию на сайте или в приложении.\n'
                    '✅ Покупает промокод.\n'
                    '✅ Предъявляет промокод при заказе услуги.\n'
                    '✅ Менеджер партнера фиксирует данный промокод.\n'
                    '✅ Пользователь получает услугу со скидкой.\n\n'
                    'ТАКОЙ ЖЕ ВНУТРЕННЕЙ АКЦИИ У ПАРТНЕРА БЫТЬ НЕ МОЖЕТ.\n\n'
                    'В результате партнер получает положительный отзыв, повторную запись, клиентскую базу, '
                    'рекомендации.',
    'page_action3': 'От партнера нужна скидка 50% (которая будет работать только на нашем сайте). '
                    'Цена со скидкой играет ключевое значение для успеха акции. Так же влияют месторасположение, отзывы пользователей, преимущества компании. '
                    'Со вторго месяца можно скидку уменьшать.\n'
                    'Рабочий вариант 50/40/30.\n '
                    'Для увеличения числа клиентов рекомендуется использовать повышенную скидку на первое посещение.\n'
                    'Акция с промокодом будет опубликована в основной рубрике и тематической подрубрике.',
    'page_action4': 'Партнер сможет открыто видеть по своей акции количество просмотров'
                    ' и количество взятых промокодов, а также наблюдать😎 за своими коллегами-конкурентами.\n'
                    'Именно такой способ создания клиентской базы наиболее выгодный и прозрачный.\n'
                    '<b>Лучше платить за привлечение скидкой своим будущим клиентам, чем рекламным агенствам.</b>\n'
                    'Это рабочий инструмент и  <b>СЛИЧНЫЙ СЕКРЕТ</b>, который становится доступен многим.\n\n'
                    'Акции публикуются на сайте в общем списке акций.',
    'page_action5': '<b>Стоимсть размещения акции на сайте.\n</b>'
                    '<b>Салоны красоты (пакет 1-3 акции).</b>\n'
                    '💵 1 месяц - 128 руб.\n'
                    '💵 3 месяца - 237 руб.\n'
                    '💵 6 месяц - 356 руб.\n'
                    '💵 12 месяц - 458 руб.\n\n'
                    '<b>Косметическое отбеливание зубов. Стоматология. Медцентры.</b>\n'
                    '💵 1 месяц - 199 руб.\n'
                    '💵 3 месяца - 299 руб.\n'
                    '💵 6 месяцев - 538 руб.\n'
                    '💵 12 месяцев - 948 руб.\n\n'
                    '<b>Лазерная эпиляция.</b>\n'
                    '💵 1 месяц - 948 руб.\n',
    'page_action6': '<b>Фотоэпиляция.</b>\n'
                    '💵 1 месяц - 299 руб.\n\n'
                    '<b>Туризм, Авиатур, Визы,Санатории.</b>\n'
                    '💵 1 месяц - 128 руб.\n'
                    '💵 3 месяца - 299 руб.\n'
                    '💵 6 месяц - 474 руб.\n'
                    '💵 12 месяц - 716 руб.\n\n'
                    '<b>Еда и Развлечения (популярное).</b>\n'
                    '💵 1 месяц - 49 руб.\n'
                    '💵 3 месяца - 89 руб.\n'
                    '💵 6 месяц - 139 руб.\n'
                    '💵 12 месяц - 199 руб.\n\n'
                    '<b>Цветы живые в сезон.</b>\n'
                    '💵 1 месяц - 199 руб.\n'
    ,
    'page_action7': '<b>Рубрика «Авто». Кузовной ремонт. Диагностика. Замена масла. Ремонт.</b>\n'
                    '💵 1 месяц - 128 руб.\n'
                    '💵 3 месяца - 299 руб.\n'
                    '💵 6 месяц - 474 руб.\n'
                    '💵 12 месяц - 716 руб.\n\n'
                    '<b>Шиномонтаж.</b>\n'
                    '💵 1 месяц - 398 руб.\n'
                    '💵 3 месяца - 498 руб.\n'
                    '💵 6 месяц - 598 руб.\n'
                    '💵 12 месяц - 798 руб.\n\n'
                    '<b>Авто – Клининг - Химчистка салона и полировка кузова.</b>\n'
                    '💵 3 месяца - 357 руб.\n'
                    '💵 6 месяц - 548 руб.\n'
                    '💵 12 месяц - 948 руб.\n\n',
    'page_action8': '<b>Другие направления.</b>\n'
                    '💵 1 месяц - 128 руб.\n'
                    '💵 3 месяца - 237 руб.\n'
                    '💵 6 месяц - 360 руб.\n'
                    '💵 12 месяц - 498 руб.\n\n'
                    '<b>Специальное предложение для самозанятых.</b>\n'
                    '💵 1 месяц - 69 руб.\n'
                    '💵 3 месяца - 99 руб.\n'
                    '💵 6 месяц - 149 руб.\n'
                    '💵 12 месяц - 199 руб.\n\n'
                    '<a href="https://www.slivki.by/populyarnye-aktsii">Ссылка на сайт на лучшие акции.</a>\n',
    'page_action9': 'Акцию можно закрепить по запросам на сайте или же в топе рубрики.\n'
                    '<b>Закрепление акции с промокодом (ТОП) на 1 месяц.</b>\n'
                    '💵Рубрика или поиск, одно место - 99 руб.\n'
                    '💵Рубрика + поиск, одно место - 149 руб.\n'
                    '💵Рубрика или поиск (для тематик: Суши, Маникюр,'
                    'Шиномонтаж, Цветы, Эпиляция (один запрос, одно место, 1-8 место) - 199 руб.\n'
                    '💵Единовременно Рубрика + поиск, '
                    '(для тематик: Суши, Маникюр, Шиномонтаж, Цветы, Эпиляция (одно место, 1-8 место) - 299 руб.\n'

}



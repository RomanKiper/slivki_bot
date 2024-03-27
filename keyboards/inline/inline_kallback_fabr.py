from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MenuCallBack(CallbackData, prefix="menu"):
    level: int
    menu_name: str


def get_user_main_btns(*, level: int, sizes: tuple[int] = (1, 2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Цены/статистика🤑💵": "price_statistic",
        "О нас": "about",
        "FAQ🤯": "faq_main",
        "Блогеры👩‍🎤": "blogers-main",
        "Ссылки🔗": "links_main",
        "Контакты": "contacts_main",
        "Готовые КП": "offers_main",
    }
    for text, menu_name in btns.items():
        if menu_name == 'catalog':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level + 1, menu_name=menu_name).pack()))
        elif menu_name == 'cart':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=3, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()
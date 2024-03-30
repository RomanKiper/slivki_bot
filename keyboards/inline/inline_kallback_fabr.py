from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MenuCallBack(CallbackData, prefix="menu"):
    level: int
    menu_name: str
    category: int | None = None


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
        if menu_name == 'price_statistic':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level + 1, menu_name=menu_name).pack()))
        elif menu_name == 'faq_main':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=2, menu_name=menu_name).pack()))
        elif menu_name == 'blogers-main':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=3, menu_name=menu_name).pack()))
        elif menu_name == 'links_main':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=4, menu_name=menu_name).pack()))
        elif menu_name == 'offers_main':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=5, menu_name=menu_name).pack()))

        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()
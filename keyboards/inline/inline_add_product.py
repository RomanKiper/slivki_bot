from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# клавиатура для админки создать новый продукт, вывести все продукты.
inline_product_add_dell_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Добавить новое",
            callback_data='add_product'
        ),
        InlineKeyboardButton(
            text="Все предложения",
            callback_data='all_products_list'
        )
    ],
])

# клавиатрура в админке для формирования инлайновых кнопок
def get_callback_btns(
        *,                       # * означает автоматический запрет на передачу неименованных запретов
        btns: dict[str, str],
        sizes: tuple[int] = (2,)):

    keyboards = InlineKeyboardBuilder()

    for text, data in btns.items():
        keyboards.add(InlineKeyboardButton(text=text, callback_data=data))

    return keyboards.adjust(*sizes).as_markup()


# клавиатрура в админке для формирования url кнопок
def get_url_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (2,)):

    keyboards = InlineKeyboardBuilder()

    for text, url in btns.items():
        keyboards.add(InlineKeyboardButton(text=text, url=url))

    return keyboards.adjust(*sizes).as_markup()


# клавиатрура в админке для формирования url кнопок или инлайновых кнопок
def get_inlineMix_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (2,)):

    keyboards = InlineKeyboardBuilder()

    for text, value in btns.items():
        if "://" in value:
            keyboards.add(InlineKeyboardButton(text=text, url=value))
        else:
            keyboards.add(InlineKeyboardButton(text=text, callback_data=value))

    return keyboards.adjust(*sizes).as_markup()


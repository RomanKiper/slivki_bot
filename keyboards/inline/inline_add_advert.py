from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_product_add_dell_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Добавить предложение",
            callback_data='add'
        )
    ],
    [
        InlineKeyboardButton(
            text="Изменить предложение",
            callback_data='change_product'
        )
    ],
    [
        InlineKeyboardButton(
            text="Удалить предложение",
            callback_data='dell_product'
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад в меню",
            callback_data='back_to_menu'
        )
    ],
])
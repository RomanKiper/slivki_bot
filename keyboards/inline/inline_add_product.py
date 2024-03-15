from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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

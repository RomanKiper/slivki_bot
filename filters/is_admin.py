from aiogram.filters import Filter
from aiogram import types, Bot
from config_data.config import Config, load_config

config: Config = load_config()

class IsAdminMsg(Filter):
    def __init__(self) -> None:
        pass

    # async def __call__(self, message: types.Message) -> bool:
    #     if message.from_user.id in config.tg_bot.id_admins:
    #         return True
    #     else:
    #         await message.answer(text="Нет прав")

    async def __call__(self, message_or_callback) -> bool:
        if isinstance(message_or_callback, types.Message):
            message = message_or_callback
            if message.from_user.id in config.tg_bot.id_admins:
                return True
            # else:
            #     await message.answer(text="Нет прав")
        elif isinstance(message_or_callback, types.CallbackQuery):
            callback_query = message_or_callback
            if callback_query.from_user.id in config.tg_bot.id_admins:
                return True
            # else:
            #     await callback_query.message.answer(text="Нет прав")


# admin_router.message(Command("add"), F.text | F.command)
# @admin_router.callback_query(lambda c: c.data.startswith(""))
# async def start_handler(message_or_callback: types.Union[types.Message, CallbackQuery]):
#     if isinstance(message_or_callback, types.Message):
#         # Если это сообщение
#         message = message_or_callback
#         await message.answer(text="👇👇Добавте товар👇👇", reply_markup=inline_product_add_dell_kb)
#     elif isinstance(message_or_callback, CallbackQuery):
#         # Если это колбэк-запрос
#         callback_query = message_or_callback
#         await callback_query.message.answer(text="👇👇Добавте товар👇👇", reply_markup=inline_product_add_dell_kb)
#

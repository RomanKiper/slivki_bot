from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_add_advert import inline_product_add_dell_kb
from filters.is_admin import IsAdminMsg

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdminMsg())
admin_router.callback_query.filter(IsAdminMsg())


@admin_router.message(Command("add"), F.text| F.command)
@admin_router.callback_query(lambda c: c.data.startswith(""))
async def start_handler(message_or_callback: types.Union[types.Message, CallbackQuery]):
    if isinstance(message_or_callback, types.Message):
        # Если это сообщение
        message = message_or_callback
        await message.answer(text="👇👇Добавте товар👇👇", reply_markup=inline_product_add_dell_kb)
    elif isinstance(message_or_callback, CallbackQuery):
        # Если это колбэк-запрос
        callback_query = message_or_callback
        await callback_query.message.answer(text="👇👇Добавте товар👇👇", reply_markup=inline_product_add_dell_kb)




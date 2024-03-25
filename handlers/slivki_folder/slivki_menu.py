from aiogram import types, Router, F
from aiogram.filters import Command, or_f
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import orm_get_main_menu
from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_add_product import get_callback_btns

slivki_private_router = Router()
slivki_private_router.message.filter(ChatTypeFilter(['private']))


@slivki_private_router.message(or_f(Command('main_menu'), (F.text.lower().in_({'main_menu', 'главное меню'}))))
async def get_main_menu_list(message: types.Message, session: AsyncSession):
        main_menu_btns = await orm_get_main_menu(session)
        btns = {main_menu_btn.name: f'main_menu_btn_{main_menu_btn.id}' for main_menu_btn in main_menu_btns}
        await message.answer("В данном блоке ты можешь получить базовую инфрмацию о компании.", reply_markup=get_callback_btns(btns=btns))


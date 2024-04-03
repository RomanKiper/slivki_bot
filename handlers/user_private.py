from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import Message, InputMediaPhoto, CallbackQuery
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Banner
from database.orm_query import orm_get_products, orm_get_banner
from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_add_product import get_callback_btns
# from keyboards.inline.inline_first_menu import create_inline_kb_main_menu

from lexicon.lexicon import LEXICON_btn_main_menu, LEXICON_btn_price_statistic

from lexicon.lexicon import LEXICON_HI


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(F.text.lower().in_({'старт', 'начать', "start"}))
@user_private_router.message(CommandStart())
@user_private_router.callback_query(lambda c: c.data.startswith("main_menu"))

async def start_cmd(message_or_callback: types.Union[types.Message, CallbackQuery], session: AsyncSession):
    if isinstance(message_or_callback, types.Message):
        message = message_or_callback
        query = select(Banner).where(Banner.name == 'main')
        result = await session.execute(query)
        banner = result.scalar()
        await message.answer_photo(photo=banner.image,
                                   caption=banner.description,
                                   reply_markup=get_callback_btns(btns=LEXICON_btn_main_menu, sizes=(1,2,)))
        await message.delete()
    elif isinstance(message_or_callback, CallbackQuery):
        # Если это колбэк-запрос
        callback = message_or_callback
        query = select(Banner).where(Banner.name == 'main')
        result = await session.execute(query)
        banner = result.scalar()
        await callback.message.answer_photo(photo=banner.image,
                                   caption=banner.description,
                                   reply_markup=get_callback_btns(btns=LEXICON_btn_main_menu, sizes=(1,2,)))
        await callback.message.delete()


@user_private_router.callback_query(F.data == 'price_statistic')
async def get_list_advertising_menu(callback: types.CallbackQuery):

    await callback.message.answer(text="text", reply_markup=get_callback_btns(btns=LEXICON_btn_price_statistic, sizes=(2,)))


@user_private_router.message(F.text.lower().in_({'помощь', "help"}))
@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("Bot's help.")


@user_private_router.message(F.text.lower().in_(LEXICON_HI))
async def hi_cmd(message: types.Message):
    await message.answer("И тебя приветствую!")







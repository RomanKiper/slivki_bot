# from aiogram import types, Router, F
# from aiogram.filters import Command, or_f
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from database.orm_query import orm_get_main_menu, orm_get_price_statistic_menu
# from filters.chat_types import ChatTypeFilter
# from keyboards.inline.inline_add_product import get_callback_btns
#
# slivki_private_router = Router()
# slivki_private_router.message.filter(ChatTypeFilter(['private']))
#
#
# @slivki_private_router.message(or_f(Command('main_menu'), (F.text.lower().in_({'main_menu', 'главное меню'}))))
# async def get_main_menu_list(message: types.Message, session: AsyncSession):
#         main_menu_btns = await orm_get_main_menu(session)
#         btns = {main_menu_btn.name: f'main_menu_btn_{main_menu_btn.id}' for main_menu_btn in main_menu_btns}
#         await message.answer("В данном блоке ты можешь получить базовую инфрмацию о компании.", reply_markup=get_callback_btns(btns=btns))
#

# @user_private_router.message(F.text.lower().in_({'старт', 'начать', "start"}))
# @user_private_router.message(CommandStart())
# async def start_cmd(message: types.Message) -> None:
#     await message.answer(text="Это была команда старт")
#
#
# @user_private_router.message(F.text.lower().in_({'помощь', "help"}))
# @user_private_router.message(Command('help'))
# async def help_cmd(message: types.Message):
#     await message.answer("Bot's help.")
#
#
# @user_private_router.message(F.text.lower().in_(LEXICON_HI))
# async def hi_cmd(message: types.Message):
#     await message.answer("И тебя приветствую!")
#
# # пример фильтрации по совпадению строки
# @user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
# @user_private_router.message(Command("delivery"))
# async def delivery_cmd(message: types.Message):
#     await message.answer("Фильтр по вариантам доставки.")


#Хэндлер отлавливать id фото. Не раскоменчивать. т.к. перехватывает данные для fsm
# @user_private_router.message(F.photo)
# async def send_photo_id(message: types.Message):
#     await message.send_copy(chat_id=message.chat.id)
#     photo_id = message.photo[0].file_id
#     await message.answer(f"ID фотографии: {photo_id}")


# @user_private_router.callback_query(F.data == 'products_menu')
# async def starring_at_product(callback: types.CallbackQuery, session: AsyncSession):
#     for product in await orm_get_products(session):
#         await callback.message.answer_photo(
#             product.image,
#             caption=f"<strong>{product.name}\
#                     </strong>\n{product.description}\nСтоимость: {round(product.price, 2)}",
#
#         )
#     await callback.message.answer("ОК, вот список товаров ⏫")

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import Message

from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_first_menu import create_inline_kb_main_menu

from lexicon.lexicon import LEXICON_HI
from keyboards.reply.reply_main_menu import start_kb, del_kb

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(F.text.lower().in_({'старт', 'начать', "start"}))
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer(text="Это была команда старт", reply_markup=start_kb)



@user_private_router.message(or_f(Command('main_menu'), (F.text.lower().in_({'main_menu', 'главное меню'}))))
async def get_main_menu(message: Message):
    keyboard = create_inline_kb_main_menu(2, 'btn_main_menu_1', 'btn_main_menu_3', 'btn_main_menu_2',
                                          'btn_main_menu_4',
                                          'btn_contract_links', 'download_app', 'btn_main_menu_5')
    await message.answer(
        text='В данном блоке ты можешь получить базовую инфрмацию о компании.',
        reply_markup=keyboard
    )
    await message.delete()


@user_private_router.message(F.text.lower().in_({'о нас', 'описание', "about"}))
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("Bot's description.")


@user_private_router.message(F.text.lower().in_({'ссылки', 'our_media', "links"}))
@user_private_router.message(Command('our_media'))
async def our_media_cmd(message: types.Message):
    await message.answer("Links for our media.")


@user_private_router.message(F.text.lower().in_({'помощь', "help"}))
@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("Bot's help.")


@user_private_router.message(F.text.lower().in_(LEXICON_HI))
async def hi_cmd(message: types.Message):
    await message.answer("И тебя приветствую!")

# пример фильтрации по совпадению строки
@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command("delivery"))
async def delivery_cmd(message: types.Message):
    await message.answer("Фильтр по вариантам доставки.")


@user_private_router.message(F.photo)
async def send_photo_id(message: types.Message):
    await message.send_copy(chat_id=message.chat.id)
    photo_id = message.photo[0].file_id
    await message.answer(f"ID фотографии: {photo_id}")





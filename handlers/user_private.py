from aiogram import types, Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Banner
from database.orm_query import orm_get_faqs, orm_get_faq, orm_add_user, orm_increment_handler_counter
from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_add_product import get_callback_btns, get_inlineMix_btns, \
    get_callback_btns_extra_btn
from lexicon.lexicon import LEXICON_btn_main_menu, LEXICON_btn_price_statistic, \
    LEXICON_btn_main_links, LEXICON_btn_slivki_site_link, LEXICON_btn_back_menu_links, LEXICON_btn_app_link, \
    LEXICON_btn_back_to_main_menu, LEXICON_btn_back_to_advertising_menu
from lexicon.lexicon import LEXICON_HI, LEXICON_RU

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(F.text.lower().in_({'старт', 'начать', "start"}))
@user_private_router.message(CommandStart())
@user_private_router.callback_query(lambda c: c.data.startswith("main_menu"))
async def start_cmd(message_or_callback: types.Union[types.Message, CallbackQuery], session: AsyncSession):
    if isinstance(message_or_callback, types.Message):
        message = message_or_callback
        await orm_add_user(session,
                           user_id=message.from_user.id,
                           username=message.from_user.username,
                           first_name=message.from_user.first_name,
                           last_name=message.from_user.last_name,
                           )
        await orm_increment_handler_counter(session,
                                            user_id=message.from_user.id,
                                            handler_name='start',
                                            username=message.from_user.username,
                                            first_name=message.from_user.first_name,
                                            last_name=message.from_user.last_name,
                                            )
        query = select(Banner).where(Banner.name == 'main')
        result = await session.execute(query)
        banner = result.scalar()
        await message.answer_photo(photo=banner.image,
                                   caption=banner.description,
                                   reply_markup=get_callback_btns(btns=LEXICON_btn_main_menu, sizes=(1, 2,)))
        await message.delete()
    elif isinstance(message_or_callback, CallbackQuery):
        # Если это колбэк-запрос
        callback = message_or_callback
        await orm_add_user(session,
                           user_id=callback.message.from_user.id,
                           username=callback.message.from_user.username,
                           first_name=callback.message.from_user.first_name,
                           last_name=callback.message.from_user.last_name,
                           )
        query = select(Banner).where(Banner.name == 'main')
        result = await session.execute(query)
        banner = result.scalar()
        await callback.message.answer_photo(photo=banner.image,
                                            caption=banner.description,
                                            reply_markup=get_callback_btns(btns=LEXICON_btn_main_menu, sizes=(1, 2,)))
        await callback.message.delete()


@user_private_router.callback_query(F.data == 'price_statistic')
async def get_list_advertising_menu(callback: types.CallbackQuery):
    await callback.message.answer(text="В данном блоке ты получшиь цены, статистику и примеры размещения рекламы.",
                                  reply_markup=get_callback_btns(btns=LEXICON_btn_price_statistic, sizes=(2,)))
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'about')
async def get_info_about(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/description_slivki'],
                                  reply_markup=get_callback_btns(btns=LEXICON_btn_back_to_main_menu, sizes=(2,)))
    await callback.message.delete()


@user_private_router.message(F.text.lower().in_(LEXICON_HI))
async def hi_cmd(message: types.Message):
    await message.answer("И тебя приветствую!")


############################################## часто задаваемые вопросы в общем доступе ###################
@user_private_router.callback_query(F.data == 'faq_main')
async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
    faqs = await orm_get_faqs(session)
    if len(faqs) > 0:
        btns = {faq.name: f'faq2_{faq.id}' for faq in faqs}
        back_to_main_menu = InlineKeyboardButton(text="НАЗАД", callback_data="main_menu")
        markup = get_callback_btns_extra_btn(btns=btns, extra_buttons=[back_to_main_menu])
        await callback.message.answer("Часто задаваемые вопросы:", reply_markup=markup)
    else:
        await callback.message.answer(
            "Список часто задаваемых вопросв пуст🤔.\nДобавьте вопросы через администартивную панель.📝")


@user_private_router.callback_query(F.data.startswith('faq2_'))
async def starring_at_product(callback: types.CallbackQuery, session: AsyncSession):
    faq_id = callback.data.split('_')[-1]
    faq_item = await orm_get_faq(session, int(faq_id))
    await callback.message.answer(
        f"<strong>{faq_item.name}</strong>\n\n"
        f"{faq_item.description}\n\n",
        reply_markup=get_callback_btns(
            btns={
                "Назад": f"faq_main",
            },
            sizes=(2,)
        ),
    )
    await callback.answer()


######################################ссылки ######################################

@user_private_router.callback_query(F.data == 'links_main')
async def get_main_menu_links(callback: types.CallbackQuery):
    await callback.message.answer(text="Рабочие ссылки компании.",
                                  reply_markup=get_callback_btns(btns=LEXICON_btn_main_links, sizes=(1, 2, 2, 2, 2, 1)))
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'site_slivki_link')
async def get_site_slivki_link(callback: types.CallbackQuery):
    await callback.message.answer(text="Ссылка на сайт Сливки Бай",
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_slivki_site_link, sizes=(1,)))
    disable_web_page_preview = True
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'app-link')
async def get_app_link(callback: types.CallbackQuery):
    await callback.message.answer(text="Ссылка на скачивание мобильного приложения slivkiby",
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_app_link, sizes=(1,)))
    disable_web_page_preview = True
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'insta_all_links')
async def get_all_insta_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/insta_links'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)))
    await callback.message.delete()


@user_private_router.message(Command('insta_links'))
async def get_all_insta_links(message: types.Message):
    await message.answer(text=LEXICON_RU['/insta_links'], disable_web_page_preview=True,
                         reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_to_advertising_menu, sizes=(1,)))
    await message.delete()


@user_private_router.callback_query(F.data == 'tiktok_all_links')
async def get_all_tiktok_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/tiktok_links'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)))
    await callback.message.delete()


@user_private_router.message(Command('tiktok_links'))
async def get_all_tiktok_links(message: types.Message):
    await message.answer(text=LEXICON_RU['/tiktok_links'], disable_web_page_preview=True,
                         reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_to_advertising_menu, sizes=(1,)))
    await message.delete()


@user_private_router.callback_query(F.data == 'telegram_all_links')
async def get_all_telegram_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/telega_links'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)))
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'agreement_links')
async def get_agreement_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/agreement_links'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)))
    await callback.message.delete()


# перенес в admin_add_product  для того чтобы досту был только у админов
# @user_private_router.callback_query(F.data == 'tables_links')
# async def get_tables_links(callback: types.CallbackQuery):
#     await callback.message.answer(text=LEXICON_RU['/list_links_work_tables'], disable_web_page_preview=True,
#                                   reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)) )
#     await callback.message.delete()


###################################################################

@user_private_router.callback_query(F.data == 'contacts_main')
async def inline_get_office_information(callback: types.CallbackQuery, bot: Bot):
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=53.904278,
                            longitude=27.569655)
    await callback.message.answer(text=LEXICON_RU['/office_adress'],
                                  reply_markup=get_callback_btns(btns=LEXICON_btn_back_to_main_menu, sizes=(2,)))
    await callback.message.delete()

#################################################################


# @user_private_router.message()
# async def send_echo(message: Message):
#     try:
#         if message.photo:
#             await message.send_copy(chat_id=message.chat.id)
#             photo_id = message.photo[0].file_id
#             await message.answer(f"ID фотографии: {photo_id}")
#         elif message.video:
#             await message.send_copy(chat_id=message.chat.id)
#             video_id = message.video.file_id
#             await message.answer(f"ID видео: {video_id}")
#     except TypeError:
#         await message.reply(text=LEXICON_RU['no_echo'])

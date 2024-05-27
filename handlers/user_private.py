from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import Message, InputMediaPhoto, CallbackQuery, InlineKeyboardButton
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Banner
from database.orm_query import orm_get_products, orm_get_banner, orm_get_faqs, orm_get_faq
from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_add_product import get_callback_btns, get_url_btns, get_inlineMix_btns, \
    get_callback_btns_extra_btn
# from keyboards.inline.inline_first_menu import create_inline_kb_main_menu

from lexicon.lexicon import LEXICON_btn_main_menu, LEXICON_btn_price_statistic, LEXICON_btn_description, \
    LEXICON_btn_main_links, LEXICON_btn_slivki_site_link, LEXICON_btn_back_menu_links, LEXICON_btn_app_link

from lexicon.lexicon import LEXICON_HI, LEXICON_RU


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
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'about')
async def get_info_about(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/description_slivki'], reply_markup=get_callback_btns(btns=LEXICON_btn_description, sizes=(2,)))
    await callback.message.delete()


@user_private_router.message(F.text.lower().in_({'помощь', "help"}))
@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("Bot's help.")


@user_private_router.message(F.text.lower().in_(LEXICON_HI))
async def hi_cmd(message: types.Message):
    await message.answer("И тебя приветствую!")


############################################## часто задаваемые вопросы в общем доступе ###################
@user_private_router.callback_query(F.data == 'faq_main')
async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
    faqs = await orm_get_faqs(session)
    btns = {faq.name: f'faq2_{faq.id}' for faq in faqs}

    back_to_main_menu = InlineKeyboardButton(text="Назад", callback_data="main_menu")
    markup = get_callback_btns_extra_btn(btns=btns, extra_buttons=[back_to_main_menu])

    await callback.message.answer("Часто задаваемые вопросы:", reply_markup=markup)


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
    await callback.message.answer(text="Рабочие ссылки компании.", reply_markup=get_callback_btns(btns=LEXICON_btn_main_links, sizes=(1,2,2,2,2,1)))
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'site_slivki_link')
async def get_site_slivki_link(callback: types.CallbackQuery):
    await callback.message.answer(text="Ссылка на сайт Сливки Бай", reply_markup=get_inlineMix_btns(btns=LEXICON_btn_slivki_site_link, sizes=(1,)) )
    disable_web_page_preview = True
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'app-link')
async def get_app_link(callback: types.CallbackQuery):
    await callback.message.answer(text="Ссылка на скачивание мобильного приложения slivkiby", reply_markup=get_inlineMix_btns(btns=LEXICON_btn_app_link, sizes=(1,)) )
    disable_web_page_preview = True
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'insta_all_links')
async def get_all_insta_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/insta_links'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)) )
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'tiktok_all_links')
async def get_all_tiktok_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/tiktok_links'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)) )
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'telegram_all_links')
async def get_all_telegram_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/telega_links'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)) )
    await callback.message.delete()


@user_private_router.callback_query(F.data == 'agreement_links')
async def get_agreement_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/agreement_links'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)) )
    await callback.message.delete()


# перенес в admin_add_product  для того чтобы досту был только у админов
# @user_private_router.callback_query(F.data == 'tables_links')
# async def get_tables_links(callback: types.CallbackQuery):
#     await callback.message.answer(text=LEXICON_RU['/list_links_work_tables'], disable_web_page_preview=True,
#                                   reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)) )
#     await callback.message.delete()
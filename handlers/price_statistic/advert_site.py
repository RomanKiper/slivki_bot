from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup

from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_add_product import get_inlineMix_btns
from lexicon.lexicon import LEXICON_PRICE, LEXICON_PROMOCOD_INFO, LEXICON_btn_back_to_advertising_menu

user_advert_router = Router()
user_advert_router.message.filter(ChatTypeFilter(['private']))


#################### telegram #########################

@user_advert_router.callback_query(F.data == 'telegram_sl')
async def on_start_telegram(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=LEXICON_PRICE['photo_telejka'],
                         caption=LEXICON_PRICE['telejka_info'],
                         reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_to_advertising_menu, sizes=(1,))
    )

##########################site###########################


first_photo = LEXICON_PRICE['first_photo']
photo_podlojka = LEXICON_PRICE['photo_podlojka']
banner_top = LEXICON_PRICE['banner_top']
brendbox = LEXICON_PRICE['brendbox']
brendbox_heading = LEXICON_PRICE['brendbox_heading']
brendbox_heading_new = LEXICON_PRICE['brendbox_heading_new']
floating = LEXICON_PRICE['floating']
banner_horizontal = LEXICON_PRICE['banner_horizontal']
advertising_news = LEXICON_PRICE['advertising_news']
brendbox_premium = LEXICON_PRICE["brendbox_premium"]


# Список ID фотографий
photo_site_ids = [first_photo, photo_podlojka, banner_top, brendbox, brendbox_heading, brendbox_heading_new, floating, banner_horizontal, advertising_news,  brendbox_premium]

caption_site_dict = {
    first_photo: LEXICON_PRICE['first_photo_info'],
    photo_podlojka: LEXICON_PRICE['podlojka_info'],
    banner_top: LEXICON_PRICE['banner_top_info'],
    brendbox: LEXICON_PRICE['brendbox_info'],
    brendbox_heading: LEXICON_PRICE['brendbox_heading_info'],
    brendbox_heading_new: LEXICON_PRICE['brendbox_heading_info_new'],
    floating: LEXICON_PRICE['floating_info'],
    banner_horizontal: LEXICON_PRICE['banner_horizontal_info'],
    advertising_news: LEXICON_PRICE['advertising_news_info'],
    brendbox_premium: LEXICON_PRICE['brendbox_premium_info'],
}

current_photo_site = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='price_statistic')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'site_slivki_advertising')
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_site_ids[current_photo_site],
                         caption=caption_site_dict[photo_site_ids[current_photo_site]],
                         reply_markup=markup_prev_next)


# Обработчик инлайн кнопки "Следующее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_photo')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_site
    current_photo_site = (current_photo_site + 1) % len(photo_site_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_site_ids[current_photo_site],
                                     caption=caption_site_dict[photo_site_ids[current_photo_site]],
                                 ),
                                 reply_markup=markup_prev_next)


# Обработчик инлайн кнопки "Предыдущее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_photo')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_site
    current_photo_site = (current_photo_site - 1) % len(photo_site_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_site_ids[current_photo_site],
                                     caption=caption_site_dict[photo_site_ids[current_photo_site]],
                                 ),
                                 reply_markup=markup_prev_next)


################################# insta ################################

# from aiogram import Router, F, types, Bot
# from aiogram.types import Message, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# from lexicon.lexicon import LEXICON_PRICE, LEXICON_btn_main_menu
#
# router = Router()

insta1 = LEXICON_PRICE['insta1']
insta2 = LEXICON_PRICE['insta2']
insta3 = LEXICON_PRICE['insta3']
insta4 = LEXICON_PRICE['insta4']
insta5 = LEXICON_PRICE['insta5']


# Список ID фотографий
photo_insta_id = [insta1, insta2, insta3, insta4, insta5]

caption_insta_dict = {
    insta1: LEXICON_PRICE['insta_info1'],
    insta2: LEXICON_PRICE['insta_info2'],
    insta3: LEXICON_PRICE['insta_info3'],
    insta4: LEXICON_PRICE['insta_info4'],
    insta5: LEXICON_PRICE['insta_info5'],
}

current_photo_insta = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo_insta')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo_insta')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='price_statistic')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_insta = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'instagram_sl')
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_insta_id[current_photo_insta],
                         caption=caption_insta_dict[photo_insta_id[current_photo_insta]],
                         reply_markup=markup_prev_next_insta)


# Обработчик инлайн кнопки "Следующее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_photo_insta')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_insta
    current_photo_insta = (current_photo_insta + 1) % len(photo_insta_id)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_insta_id[current_photo_insta],
                                     caption=caption_insta_dict[photo_insta_id[current_photo_insta]],
                                 ),
                                 reply_markup=markup_prev_next_insta)


# Обработчик инлайн кнопки "Предыдущее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_photo_insta')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_insta
    current_photo_insta = (current_photo_insta - 1) % len(photo_insta_id)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_insta_id[current_photo_insta],
                                     caption=caption_insta_dict[photo_insta_id[current_photo_insta]],
                                 ),
                                 reply_markup=markup_prev_next_insta)

################# tik tok #####################

tiktok1 = LEXICON_PRICE['tiktok1']
tiktok2 = LEXICON_PRICE['tiktok2']

text_tiktok = [tiktok1, tiktok2]

current_text_tiktok = 0

button_next = InlineKeyboardButton(
    text='Далее',
    callback_data='next_page_tik')
button_prev = InlineKeyboardButton(
    text='Назад',
    callback_data='prev_page_tik')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='price_statistic')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_tik_tik = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'tiktok_sl')
async def on_start(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id,
                           text=text_tiktok[current_text_tiktok],
                           reply_markup=markup_prev_next_tik_tik)


# Обработчик инлайн кнопки "Следующеая страница"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_page_tik')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_text_tiktok
    current_text_tiktok = (current_text_tiktok + 1) % len(text_tiktok)
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=text_tiktok[current_text_tiktok],
                                reply_markup=markup_prev_next_tik_tik,
                                disable_web_page_preview=True)


# Обработчик инлайн кнопки "Предыдущий техт"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_page_tik')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_text_tiktok
    current_text_tiktok = (current_text_tiktok - 1) % len(text_tiktok)
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=text_tiktok[current_text_tiktok],
                                reply_markup=markup_prev_next_tik_tik,
                                disable_web_page_preview=True)


########################### promotion #####################

action1 = LEXICON_PROMOCOD_INFO['page_action1']
action2 = LEXICON_PROMOCOD_INFO['page_action2']
action3 = LEXICON_PROMOCOD_INFO['page_action3']
action4 = LEXICON_PROMOCOD_INFO['page_action4']
action5 = LEXICON_PROMOCOD_INFO['page_action5']
action6 = LEXICON_PROMOCOD_INFO['page_action6']
action7 = LEXICON_PROMOCOD_INFO['page_action7']
action8 = LEXICON_PROMOCOD_INFO['page_action8']
action9 = LEXICON_PROMOCOD_INFO['page_action9']


text_pages = [action1, action2, action3, action4, action5, action6, action7, action8, action9]

current_text_index = 0

button_next = InlineKeyboardButton(
    text='Далее',
    callback_data='next_page_action')
button_prev = InlineKeyboardButton(
    text='Назад',
    callback_data='prev_page_action')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='price_statistic')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_promotion = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'site_slivki_promotion')
async def on_start(message: Message, bot: Bot):
    disable_web_page_preview = True
    await bot.send_message(chat_id=message.from_user.id,
                           text=text_pages[current_text_index],
                           reply_markup=markup_prev_next_promotion)


# Обработчик инлайн кнопки "Следующеая страница"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_page_action')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_text_index
    current_text_index = (current_text_index + 1) % len(text_pages)
    disable_web_page_preview = True
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=text_pages[current_text_index],
                                reply_markup=markup_prev_next_promotion,
                                disable_web_page_preview=True)


# Обработчик инлайн кнопки "Предыдущий техт"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_page_action')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_text_index
    current_text_index = (current_text_index - 1) % len(text_pages)
    disable_web_page_preview = True
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=text_pages[current_text_index],
                                reply_markup=markup_prev_next_promotion,
                                disable_web_page_preview=True)

################################### app #################################

app1 = LEXICON_PRICE['app1']
app2 = LEXICON_PRICE['app2']
app3 = LEXICON_PRICE['app3']
app4 = LEXICON_PRICE['app4']


# Список ID фотографий
photo_ids = [app1, app2, app3, app4]

caption_dict = {
    app1: LEXICON_PRICE['app_info1'],
    app2: LEXICON_PRICE['app_info2'],
    app3: LEXICON_PRICE['app_info3'],
    app4: LEXICON_PRICE['app_info4'],
}

current_photo_index = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo_app')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo_app')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='price_statistic')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_app = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'app_advertising')
# async def on_start(message: Message, bot: Bot):
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_ids[current_photo_index],
                         caption=caption_dict[photo_ids[current_photo_index]],
                         reply_markup=markup_prev_next_app)


# Обработчик инлайн кнопки "Следующее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_photo_app')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index + 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_app)


# Обработчик инлайн кнопки "Предыдущее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_photo_app')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index - 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_app)


###########################  regions  #####################

region_page1 = LEXICON_PRICE['region_page1']
region_page2 = LEXICON_PRICE['region_page2']
region_page3 = LEXICON_PRICE['region_page3']
region_page4 = LEXICON_PRICE['region_page4']

text_regions = [region_page1, region_page2, region_page3, region_page4]

current_text_regions = 0

button_next = InlineKeyboardButton(
    text='Далее',
    callback_data='next_page_region')
button_prev = InlineKeyboardButton(
    text='Назад',
    callback_data='prev_page_region')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='price_statistic')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_regions = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'regions_sl')
async def on_start(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id,
                           text=text_regions[current_text_regions],
                           reply_markup=markup_prev_next_regions)


# Обработчик инлайн кнопки "Следующеая страница"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_page_region')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_text_regions
    current_text_regions = (current_text_regions + 1) % len(text_regions)
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=text_regions[current_text_regions],
                                reply_markup=markup_prev_next_regions,
                                disable_web_page_preview=True)


# Обработчик инлайн кнопки "Предыдущий техт"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_page_region')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_text_regions
    current_text_regions = (current_text_regions - 1) % len(text_regions)
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=text_regions[current_text_regions],
                                reply_markup=markup_prev_next_regions,
                                disable_web_page_preview=True)
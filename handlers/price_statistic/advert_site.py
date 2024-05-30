from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup

from filters.chat_types import ChatTypeFilter
from lexicon.lexicon import LEXICON_PRICE, LEXICON_btn_main_menu

user_advert_router = Router()
user_advert_router.message.filter(ChatTypeFilter(['private']))

first_photo = LEXICON_PRICE['first_photo']
photo_podlojka1 = LEXICON_PRICE['photo_podlojka1']
photo_podlojka2 = LEXICON_PRICE['photo_podlojka2']
photo_podlojka3 = LEXICON_PRICE['photo_podlojka3']
banner_top1 = LEXICON_PRICE['banner_top1']
banner_top2 = LEXICON_PRICE['banner_top2']
banner_top3 = LEXICON_PRICE['banner_top3']
brendbox1 = LEXICON_PRICE['brendbox1']
brendbox2 = LEXICON_PRICE['brendbox2']
brendbox3 = LEXICON_PRICE['brendbox3']
brendbox_heading1 = LEXICON_PRICE['brendbox_heading1']
brendbox_heading2 = LEXICON_PRICE['brendbox_heading2']
floating1 = LEXICON_PRICE['floating1']
floating2 = LEXICON_PRICE['floating2']
banner_horizontal1 = LEXICON_PRICE['banner_horizontal1']
banner_horizontal2 = LEXICON_PRICE['banner_horizontal2']
advertising_news1 = LEXICON_PRICE['advertising_news1']
advertising_news2 = LEXICON_PRICE['advertising_news2']
brendbox_premium1 = LEXICON_PRICE["brendbox_premium1"]
brendbox_premium2 = LEXICON_PRICE["brendbox_premium2"]

# Список ID фотографий
photo_ids = [first_photo, photo_podlojka1, photo_podlojka2, photo_podlojka3, banner_top1, banner_top2, banner_top3,
             brendbox1, brendbox2, brendbox3, brendbox_heading1, brendbox_heading2, floating1, floating2,
             banner_horizontal1, banner_horizontal2, advertising_news1, advertising_news2, brendbox_premium1,
             brendbox_premium2]

caption_dict = {
    first_photo: LEXICON_PRICE['first_photo_info'],
    photo_podlojka1: LEXICON_PRICE['podlojka_info'],
    photo_podlojka2: LEXICON_PRICE['podlojka_info2'],
    photo_podlojka3: LEXICON_PRICE['podlojka_info2'],
    banner_top1: LEXICON_PRICE['banner_top_info'],
    banner_top2: LEXICON_PRICE['banner_top_info2'],
    banner_top3: LEXICON_PRICE['banner_top_info2'],
    brendbox1: LEXICON_PRICE['brendbox_info'],
    brendbox2: LEXICON_PRICE['brendbox_info2'],
    brendbox3: LEXICON_PRICE['brendbox_info3'],
    brendbox_heading1: LEXICON_PRICE['brendbox_heading_info'],
    brendbox_heading2: LEXICON_PRICE['brendbox_heading_info2'],
    floating1: LEXICON_PRICE['floating_info'],
    floating2: LEXICON_PRICE['floating_info2'],
    banner_horizontal1: LEXICON_PRICE['banner_horizontal_info'],
    banner_horizontal2: LEXICON_PRICE['banner_horizontal_info2'],
    advertising_news1: LEXICON_PRICE['advertising_news_info'],
    advertising_news2: LEXICON_PRICE['advertising_news_info2'],
    brendbox_premium1: LEXICON_PRICE['brendbox_premium_info'],
    brendbox_premium2: LEXICON_PRICE['brendbox_premium_info2'],
}

current_photo_index = 0

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
    callback_data='btn_main_menu_1')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'site_slivki_advertising')
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_ids[current_photo_index],
                         caption=caption_dict[photo_ids[current_photo_index]],
                         reply_markup=markup_prev_next)


# Обработчик инлайн кнопки "Следующее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_photo')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index + 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next)


# Обработчик инлайн кнопки "Предыдущее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_photo')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index - 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next)
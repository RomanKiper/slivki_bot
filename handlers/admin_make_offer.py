import json

from aiogram import Router, F, types
from aiogram.types import UNSET_PARSE_MODE
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from sqlalchemy import select, delete

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database.models import Offer, Cart
from filters.chat_types import ChatTypeFilter
from filters.is_admin import IsAdminMsg
from database.orm_query import orm_add_user, orm_add_to_cart, orm_get_user_carts, orm_delete_all_carts, orm_get_offers,\
    orm_get_offers_id, orm_delete_offer, orm_get_product, orm_get_products_in_offer
from handlers.menu_processing import get_menu_content
from keyboards.inline.inline_add_product import get_callback_btns
from keyboards.inline.inline_offer import MenuCallBack

admin_offer_router = Router()
admin_offer_router.message.filter(ChatTypeFilter(['private']), IsAdminMsg())
admin_offer_router.callback_query.filter(IsAdminMsg())


class AddOffer(StatesGroup):
    # Шаги состояний
    name = State()
    description = State()
    making_offer = State()
    discount = State()


    offer_for_change = None


    texts = {
        'AddOffer:name': 'Введите название заново:',
        'AddOffer:description': 'Введите описание заново:',
        'AddOffer:making_offer': 'Выберите услугу заново:',
        'AddOffer:discount': 'Этот стейт последний, поэтому...',
    }


@admin_offer_router.callback_query(F.data == 'offers_list')
async def admin_get_offers_list(callback: types.CallbackQuery, session: AsyncSession):
    user_id = callback.from_user.id
    offers = await orm_get_offers(session, user_id)
    btns = {offer.name: f'offer_{offer.id}' for offer in offers}
    print(btns)
    await callback.message.answer("Архив КП", reply_markup=get_callback_btns(btns=btns, sizes=(1,)))


@admin_offer_router.callback_query(F.data.startswith('offer_'))
async def starring_at_offer(callback: types.CallbackQuery, session: AsyncSession):
    offer_id = callback.data.split('_')[-1]

    offer = await orm_get_offers_id(session, int(offer_id))

    loaded_list = offer.cart_product_list_ids
    list_json = json.loads(loaded_list)
    print(list_json, type(list_json))


    product_cards= []
    for i in list_json:
        for n, k in i.items():
            pr_id = int(n)
            pr_quantity = int(k)
            print(pr_id, type(pr_id), pr_quantity, type(pr_quantity))

            product = await orm_get_products_in_offer(session, pr_id=pr_id)
            product_card = (

                f"<strong>{product.name}</strong>\n"
                f"Описание: {product.description}\n"
                f"Стоимость услуги: {product.price}\n"
                f"Количество услуг: {pr_quantity}\n"
                f"Общая стоимсть: {product.price}*{pr_quantity}={product.price*pr_quantity}\n\n"

                #   Передать фото карточки товара.
                # # f" Фото: {product.image}\n\n"
                # f"Фото: <a href='{product.image}'><img src='{product.image}'></a>\n\n"
            )
            product_cards.append(product_card)


    await callback.message.answer(
        f"<strong>{offer.name}</strong>\n\n"
        f"{offer.description}\n\n"
        f"<strong>Предлагаемые каналы для продвижения:</strong>\n"
        
        f"{''.join(product_cards)}\n"
        
        f"Стоимость КП: {offer.price} руб.\n"
        f"Скидка: {offer.discont} %.\n"
        f"Стоимость со скидокой: {offer.price_with_discont} руб.",
        reply_markup=get_callback_btns(
            btns={
                "Удалить": f"remove_offer_{offer.id}",
                "Назад в список КП": "offers_list",
            },
            sizes=(2,)
        ),
    )
    await callback.answer()


@admin_offer_router.callback_query(F.data.startswith('remove_offer_'))
async def delete_offer_callback(callback: types.CallbackQuery, session: AsyncSession):
    offer_id = callback.data.split("_")[-1]
    user_id = callback.from_user.id
    await orm_delete_offer(session, int(offer_id), int(user_id))

    # async def orm_delete_offer(session: AsyncSession, offer_id: int, user_id: int):
    query = delete(Offer).where(Offer.user_id == user_id, Offer.id == int(offer_id))
    await session.execute(query)
    await session.commit()

    await callback.answer("КП удалено")
    await callback.message.answer("КП удалено!")


# Становимся в состояние ожидания ввода name
@admin_offer_router.callback_query(StateFilter(None), F.data == 'add_offer')
# Становимся в состояние ожидания ввода name
async def add_product(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название КП")
    await callback.message.delete()
    await state.set_state(AddOffer.name)


# Хендлер отмены и сброса состояния должен быть всегда именно хдесь.
#В нашем случае срабатывет хэндлер сброса сосояния, который находится в папке admin_add_product



# Ловим данные для состояние name и потом меняем состояние на description
@admin_offer_router.message(AddOffer.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if message.text == "." and AddOffer.offer_for_change:
        await state.update_data(name=AddOffer.offer_for_change.name)
    else:
        # Здесь можно сделать какую либо дополнительную проверку
        # и выйти из хендлера не меняя состояние с отправкой соответствующего сообщения
        # например:
        if 4 >= len(message.text) >= 150:
            await message.answer(
                "Название товара не должно превышать 150 символов\nили быть менее 5ти символов. \n Введите заново"
            )
            return

        await state.update_data(name=message.text)
    await message.answer("Введите описание КП")
    await state.set_state(AddOffer.description)

# Хендлер для отлова некорректных вводов для состояния name
@admin_offer_router.message(AddOffer.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст названия товара")


# Ловим данные для состояние description и потом меняем состояние на
@admin_offer_router.message(AddOffer.description, F.text)
async def add_description(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text == "." and AddOffer.offer_for_change:
        await state.update_data(description=AddOffer.offer_for_change.description)
    else:
        if 4 >= len(message.text):
            await message.answer(
                "Слишком короткое описание. \n Введите заново"
            )
            return
        await state.update_data(description=message.text)


    media, reply_markup = await get_menu_content(session, level=0, menu_name="offer")
    await message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)
    await state.set_state(AddOffer.making_offer)
    user = message.from_user
    await orm_delete_all_carts(session, user_id=user.id)


async def add_to_cart(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    user = callback.from_user
    await orm_add_user(
        session,
        user_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=None,
    )
    await orm_add_to_cart(session, user_id=user.id, product_id=callback_data.product_id)
    await callback.answer("Товар добавлен в корзину.")


@admin_offer_router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):

    if callback_data.menu_name == "add_to_cart":
        await add_to_cart(callback, callback_data, session)
        return

    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
        category=callback_data.category,
        page=callback_data.page,
        product_id=callback_data.product_id,
        user_id=callback.from_user.id,
    )

    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()


# Хендлер для отлова некорректных вводов для состояния description
@admin_offer_router.message(AddOffer.description)
async def add_description2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст описания КП")


async def orm_get_product_id_in_carts(session: AsyncSession, user_id):
    query = select(Cart).filter(Cart.user_id == user_id).options(joinedload(Cart.product))
    result = await session.execute(query)
    return result.scalars().all()


# Ловим callback выбора
@admin_offer_router.callback_query(AddOffer.making_offer, F.data == 'save_offer')
async def making_new_offer(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):
    await state.set_state(AddOffer.discount)
    await callback.message.answer('Введите % скилки от 0 до 99!')
    await callback.answer()


#
# #Ловим любые некорректные действия, кроме нажатия на кнопку выбора категории
# @admin_router.message(AddProduct.category)
# async def category_choice2(message: types.Message, state: FSMContext):
#     await message.answer("'Выберите катеорию из кнопок.'")
#
#
# # Ловим данные для состояние discount
@admin_offer_router.message(AddOffer.discount, F.text)
async def add_discount(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text == "." and AddOffer.offer_for_change:
        await state.update_data(discount=AddOffer.offer_for_change.discount)
    else:
        try:
            int(message.text)
        except ValueError:
            await message.answer("Введите корректное значение Скидки. Это число от 0 до 99")
            return

    await state.update_data(discount=int(message.text))
    data = await state.get_data()
    print(f"Сохраненные данные data: {data}")

    user_id = message.from_user.id
    carts = await orm_get_user_carts(session, user_id)

    product_id_quantity_list = []
    product_in_cart_price = 0
    for a in carts:
        pr_qt = {a.product.id: a.quantity}
        product_id_quantity_list.append(pr_qt)

        product_in_cart_price = round(product_in_cart_price + (a.product.price * a.quantity), 2)

        product_in_cart_price_with_discont = round(product_in_cart_price * (100 - int(message.text)) /100, 2)

        print(f" айди продукта {a.product.id}, колиичество в пакете{a.quantity}")

    print(f" Общая стоимость корзины {product_in_cart_price}")

    print(product_id_quantity_list)
    cart_product_list_ids = product_id_quantity_list
    await state.update_data(making_offer=carts)


    obj = Offer(
        name=data['name'],
        description=data['description'],
        discont=data['discount'],
        description2='making_offer',
        price=product_in_cart_price,
        price_with_discont=product_in_cart_price_with_discont,
        user_id=message.from_user.id,
    )
    obj.save_cart_product_list_ids(cart_product_list_ids)
    session.add(obj)
    await session.commit()
    await message.answer("КП добавлено/изменено", )
    await state.clear()



    # try:
    #     if AddOffer.offer_for_change:
    #         await orm_update_product(session, AddOffer.offer_for_change.id, data)
    #     else:
    #         await orm_add_offer(session, data)
    #     await message.answer("КП добавлен/изменен",)
    #     await state.clear()
    #
    # except Exception as e:
    #     await message.answer(
    #         f"Ошибка: \n{str(e)}\nОбратись к программеру, он опять денег хочет")
    #     await state.clear()
    #
    # AddOffer.product_for_change = None



# Хендлер для отлова некорректных вводов для состояния name
@admin_offer_router.message(AddOffer.discount)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("Размер ски дки может быть от 0 до 99%!")

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Offer
from filters.chat_types import ChatTypeFilter
from filters.is_admin import IsAdminMsg
from database.orm_query import orm_add_product, orm_get_products, orm_delete_product, \
    orm_update_product, orm_get_product, orm_get_categories, orm_change_banner_image, orm_get_info_pages, orm_add_user, \
    orm_add_to_cart, orm_get_user_carts, orm_add_offer
from handlers.menu_processing import get_menu_content
from keyboards.inline.inline_add_product import get_callback_btns
from keyboards.inline.inline_offer import MenuCallBack
from lexicon.lexicon import LEXICON_btn_add_offer

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
#
#
# # @admin_router.callback_query(F.data == 'products_list')
# # async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
# #     categories = await orm_get_categories(session)
# #     btns = {category.name : f'category_{category.id}' for category in categories}
# #     await callback.message.answer("Выберите категорию", reply_markup=get_callback_btns(btns=btns))
# #
# #
# # @admin_router.callback_query(F.data.startswith('category_'))
# # async def starring_at_product(callback: types.CallbackQuery, session: AsyncSession):
# #     category_id = callback.data.split('_')[-1]
# #     for product in await orm_get_products(session, int(category_id)):
# #         await callback.message.answer_photo(
# #             product.image,
# #             caption=f"<strong>{product.name}\
# #                     </strong>\n{product.description}\nСтоимость: {round(product.price, 2)}",
# #             reply_markup=get_callback_btns(
# #                 btns={
# #                     "Удалить": f"delete_{product.id}",
# #                     "Изменить": f"change_{product.id}",
# #                 },
# #                 sizes=(2,)
# #             ),
# #         )
# #     await callback.answer()
# #     await callback.message.answer("ОК, вот список товаров ⏫")
# #
# #
# # @admin_router.callback_query(F.data.startswith("delete_"))
# # async def delete_product_callback(callback: types.CallbackQuery, session: AsyncSession):
# #     product_id = callback.data.split("_")[-1]
# #     await orm_delete_product(session, int(product_id))
# #
# #     await callback.answer("Товар удален")
# #     await callback.message.answer("Товар удален!")
# #
# # # FSM:
# #
# # @admin_router.callback_query(StateFilter(None), F.data.startswith("change_"))
# # async def change_product_callback(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):
# #     product_id = callback.data.split("_")[-1]
# #     product_for_change = await orm_get_product(session, int(product_id))
# #     AddProduct.product_for_change = product_for_change
# #     await callback.answer()
# #     await callback.message.answer(
# #         "Введите название товара", reply_markup=types.ReplyKeyboardRemove()
# #     )
# #     await state.set_state(AddProduct.name)
# #
# #
# Становимся в состояние ожидания ввода name
@admin_offer_router.callback_query(StateFilter(None), F.data == 'add_offer')
# Становимся в состояние ожидания ввода name
async def add_product(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название КП")
    await callback.message.delete()
    await state.set_state(AddOffer.name)
#
#
# Хендлер отмены и сброса состояния должен быть всегда именно хдесь,
# после того как только встали в состояние номер 1 (элементарная очередность фильтров)
@admin_offer_router.message(StateFilter("*"), Command("отмена"))
@admin_offer_router.message(StateFilter("*"), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    if AddOffer.product_for_change:
        AddOffer.offer_for_change = None
    await state.clear()
    await message.answer("Действия отменены", reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))


# Вернутся на шаг назад (на прошлое состояние)
@admin_offer_router.message(StateFilter("*"), Command("назад"))
@admin_offer_router.message(StateFilter("*"), F.text.casefold() == "назад")
async def back_step_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()

    if current_state == AddOffer.name:
        await message.answer(
            'Предидущего шага нет, или введите название товара или напишите "отмена"'
        )
        return



    previous = None
    for step in AddOffer.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(
                f"Ок, вы вернулись к прошлому шагу \n {AddOffer.texts[previous.state]}"
            )
            return
        previous = step
#
#
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
    await message.answer("Введите описание товара")
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


# Ловим callback выбора
@admin_offer_router.callback_query(AddOffer.making_offer, F.data == 'save_offer')
async def making_new_offer(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):
    user_id = callback.from_user.id
    carts = await orm_get_user_carts(session, user_id)

    await state.update_data(making_offer=carts)

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
    print(f"тесттесттесттест{data}")


    obj = Offer(
        name=data['name'],
        description=data['description'],
        discont=data['discount'],
        description2=data['making_offer'],
        price=99999,
        price_with_discont=88888,
        user_id=message.from_user.id


        # category_id=int(data["category"]),
    )
    session.add(obj)
    await session.commit()
    await message.answer("КП добавлен/изменен", )
    await state.clear()

    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # name: Mapped[str] = mapped_column(String(150), nullable=False)
    # description: Mapped[str] = mapped_column(Text)
    # description2: Mapped[str] = mapped_column(Text)
    # price: Mapped[float] = mapped_column(Numeric(5,2), nullable=False)
    # price_with_discont: Mapped[float] = mapped_column(Numeric(5,2), nullable=False)
    # discont: Mapped[int]
    # user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    # cart_id: Mapped[int] = mapped_column(ForeignKey('cart.id', ondelete='CASCADE'), nullable=False)

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
#
#
# # Ловим данные для состояние image и потом выходим из состояний
# @admin_router.message(AddProduct.image, or_f(F.photo, F.text == "."))
# async def add_image(message: types.Message, state: FSMContext, session: AsyncSession):
#     if message.text and message.text == "." and AddProduct.product_for_change:
#         await state.update_data(image=AddProduct.product_for_change.image)
#
#     elif message.photo:
#         await state.update_data(image=message.photo[-1].file_id)
#     else:
#         await message.answer("Отправьте фото предложения!")
#         return
#     data = await state.get_data()
#     try:
#         if AddProduct.product_for_change:
#             await orm_update_product(session, AddProduct.product_for_change.id, data)
#         else:
#             await orm_add_product(session, data)
#         await message.answer("Товар добавлен/изменен", reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))
#         await state.clear()
#
#     except Exception as e:
#         await message.answer(
#             f"Ошибка: \n{str(e)}\nОбратись к программеру, он опять денег хочет",
#             reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)),
#         )
#         await state.clear()
#
#     AddProduct.product_for_change = None
#
# # Ловим все прочее некорректное поведение для этого состояния
# @admin_router.message(AddProduct.image)
# async def add_image2(message: types.Message, state: FSMContext):
#     await message.answer("Отправьте фото пищи")
#
#
# ################# Микро FSM для загрузки/изменения баннеров ############################
#
# class AddBanner(StatesGroup):
#     image = State()
#
# # Отправляем перечень информационных страниц бота и становимся в состояние отправки photo
# @admin_router.callback_query(StateFilter(None), F.data == 'add_change_banner')
# async def add_image2(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):
#     pages_names = [page.name for page in await orm_get_info_pages(session)]
#     await callback.message.answer(f"Отправьте фото баннера.\nВ описании укажите для какой страницы:\
#                          \n{', '.join(pages_names)}")
#     await state.set_state(AddBanner.image)
#
# # Добавляем/изменяем изображение в таблице (там уже есть записанные страницы по именам:
# # main, catalog, cart(для пустой корзины), about, payment, shipping
# @admin_router.message(AddBanner.image, F.photo)
# async def add_banner(message: types.Message, state: FSMContext, session: AsyncSession):
#     image_id = message.photo[-1].file_id
#     for_page = message.caption.strip()
#     pages_names = [page.name for page in await orm_get_info_pages(session)]
#     if for_page not in pages_names:
#         await message.answer(f"Введите нормальное название страницы, например:\
#                          \n{', '.join(pages_names)}")
#         return
#     await orm_change_banner_image(session, for_page, image_id,)
#     await message.answer("Баннер добавлен/изменен.")
#     await state.clear()
#
# # ловим некоррекный ввод
# @admin_router.message(AddBanner.image)
# async def add_banner2(message: types.Message, state: FSMContext):
#     await message.answer("Отправьте фото баннера или отмена")
#
# #######################################################################################
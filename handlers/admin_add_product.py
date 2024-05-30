from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession

from filters.chat_types import ChatTypeFilter
from filters.is_admin import IsAdminMsg
from database.orm_query import orm_add_product, orm_get_products, orm_delete_product, \
    orm_update_product, orm_get_product, orm_get_categories, orm_change_banner_image, orm_get_info_pages
from keyboards.inline.inline_add_product import get_callback_btns, get_inlineMix_btns
from lexicon.lexicon import LEXICON_btn_main_admin_menu, LEXICON_RU, LEXICON_btn_back_menu_links

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdminMsg())
admin_router.callback_query.filter(IsAdminMsg())


class AddProduct(StatesGroup):
    # Шаги состояний
    name = State()
    description = State()
    category = State()
    price = State()
    image = State()

    product_for_change = None

    texts = {
        'AddProduct:name': 'Введите название заново:',
        'AddProduct:description': 'Введите описание заново:',
        'AddProduct:price': 'Введите стоимость заново:',
        'AddProduct:image': 'Этот стейт последний, поэтому...',
    }


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


class Add_FAQ(StatesGroup):
    # Шаги состояний
    name = State()
    description = State()

    texts = {
        'Add_FAQ:name': 'Введите название заново:',
        'Add_FAQ:description': 'Введите описание заново:',
    }


class AddNote(StatesGroup):
    # Шаги состояний
    name = State()
    description = State()

    texts = {
        'AddNote:name': 'Введите название заново:',
        'AddNote:description': 'Введите описание заново:',
    }


class Add_price(StatesGroup):
    # Шаги состояний
    name = State()
    price = State()

    texts = {
        'Add_price:name': 'Введите название прайса или комментарий к прайсу заново:',
        'Add_price:price': 'Загрузите прайс заново:',
    }


class Add_document(StatesGroup):
    # Шаги состояний
    name = State()
    document = State()

    texts = {
        'Add_document:name': 'Введите название документа или комментарий к документу заново:',
        'Add_document:document': 'Загрузите прайс заново:',
    }


@admin_router.message(Command("admin"), F.text| F.command)
@admin_router.callback_query(lambda c: c.data.startswith("admin"))
async def admin_handler(message_or_callback: types.Union[types.Message, CallbackQuery]):
    if isinstance(message_or_callback, types.Message):
        # Если это сообщение
        message = message_or_callback
        await message.answer(text=LEXICON_RU["/admin+panel"], reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))
    elif isinstance(message_or_callback, CallbackQuery):
        # Если это колбэк-запрос
        callback_query = message_or_callback
        await callback_query.message.answer(text=LEXICON_RU["/admin+panel"], reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))


@admin_router.callback_query(F.data == 'products_list')
async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
    categories = await orm_get_categories(session)
    btns = {category.name : f'category_{category.id}' for category in categories}
    await callback.message.answer("Выберите категорию", reply_markup=get_callback_btns(btns=btns))


@admin_router.callback_query(F.data.startswith('category_'))
async def starring_at_product(callback: types.CallbackQuery, session: AsyncSession):
    category_id = callback.data.split('_')[-1]
    for product in await orm_get_products(session, int(category_id)):
        await callback.message.answer_photo(
            product.image,
            caption=f"<strong>{product.name}\
                    </strong>\n{product.description}\nСтоимость: {round(product.price, 2)}",
            reply_markup=get_callback_btns(
                btns={
                    "Удалить": f"delete_{product.id}",
                    "Изменить": f"change_{product.id}",
                },
                sizes=(2,)
            ),
        )
    await callback.answer()
    await callback.message.answer("ОК, вот список товаров ⏫")


@admin_router.callback_query(F.data.startswith("delete_"))
async def delete_product_callback(callback: types.CallbackQuery, session: AsyncSession):
    product_id = callback.data.split("_")[-1]
    await orm_delete_product(session, int(product_id))

    await callback.answer("Товар удален")
    await callback.message.answer("Товар удален!")

# FSM:

@admin_router.callback_query(StateFilter(None), F.data.startswith("change_"))
async def change_product_callback(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):
    product_id = callback.data.split("_")[-1]
    product_for_change = await orm_get_product(session, int(product_id))
    AddProduct.product_for_change = product_for_change
    await callback.answer()
    await callback.message.answer(
        "Введите название товара", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(AddProduct.name)


# Становимся в состояние ожидания ввода name
@admin_router.callback_query(StateFilter(None), F.data == 'add_product')
# Становимся в состояние ожидания ввода name
async def add_product(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название товара")
    await callback.message.delete()
    await state.set_state(AddProduct.name)


# Хендлер отмены и сброса состояния должен быть всегда именно хдесь,
# после того как только встали в состояние номер 1 (элементарная очередность фильтров)
@admin_router.message(StateFilter("*"), Command("отмена"))
@admin_router.message(StateFilter("*"), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    if AddProduct.product_for_change:
        AddProduct.product_for_change = None
    await state.clear()
    await message.answer("Действия отменены", reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))


# Ловим данные для состояние name и потом меняем состояние на description
@admin_router.message(AddProduct.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if message.text == "." and AddProduct.product_for_change:
        await state.update_data(name=AddProduct.product_for_change.name)
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
    await state.set_state(AddProduct.description)

# Хендлер для отлова некорректных вводов для состояния name
@admin_router.message(AddProduct.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст названия товара")


# Ловим данные для состояние description и потом меняем состояние на category
@admin_router.message(AddProduct.description, F.text)
async def add_description(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text == "." and AddProduct.product_for_change:
        await state.update_data(description=AddProduct.product_for_change.description)
    else:
        if 4 >= len(message.text):
            await message.answer(
                "Слишком короткое описание. \n Введите заново"
            )
            return
        await state.update_data(description=message.text)

    categories = await orm_get_categories(session)
    btns = {category.name : str(category.id) for category in categories}
    await message.answer("Выберите категорию", reply_markup=get_callback_btns(btns=btns))
    await state.set_state(AddProduct.category)


# Хендлер для отлова некорректных вводов для состояния description
@admin_router.message(AddProduct.description)
async def add_description2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст описания товара")


# Ловим callback выбора категории
@admin_router.callback_query(AddProduct.category)
async def category_choice(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):
    if int(callback.data) in [category.id for category in await orm_get_categories(session)]:
        await callback.answer()
        await state.update_data(category=callback.data)
        await callback.message.answer('Теперь введите цену товара.')
        await state.set_state(AddProduct.price)
    else:
        await callback.message.answer('Выберите катеорию из кнопок.')
        await callback.answer()

#Ловим любые некорректные действия, кроме нажатия на кнопку выбора категории
@admin_router.message(AddProduct.category)
async def category_choice2(message: types.Message, state: FSMContext):
    await message.answer("'Выберите катеорию из кнопок.'")


# Ловим данные для состояние price и потом меняем состояние на image
@admin_router.message(AddProduct.price, F.text)
async def add_price(message: types.Message, state: FSMContext):
    if message.text == "." and AddProduct.product_for_change:
        await state.update_data(price=AddProduct.product_for_change.price)
    else:
        try:
            float(message.text)
        except ValueError:
            await message.answer("Введите корректное значение цены")
            return

        await state.update_data(price=message.text)
    await message.answer("Загрузите изображение товара")
    await state.set_state(AddProduct.image)

# Хендлер для отлова некорректных ввода для состояния price
@admin_router.message(AddProduct.price)
async def add_price2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите стоимость товара")


# Ловим данные для состояние image и потом выходим из состояний
@admin_router.message(AddProduct.image, or_f(F.photo, F.text == "."))
async def add_image(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text and message.text == "." and AddProduct.product_for_change:
        await state.update_data(image=AddProduct.product_for_change.image)

    elif message.photo:
        await state.update_data(image=message.photo[-1].file_id)
    else:
        await message.answer("Отправьте фото предложения!")
        return
    data = await state.get_data()
    try:
        if AddProduct.product_for_change:
            await orm_update_product(session, AddProduct.product_for_change.id, data)
        else:
            await orm_add_product(session, data)
        await message.answer("Товар добавлен/изменен", reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))
        await state.clear()

    except Exception as e:
        await message.answer(
            f"Ошибка: \n{str(e)}\nОбратись к программеру, он опять денег хочет",
            reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)),
        )
        await state.clear()

    AddProduct.product_for_change = None

# Ловим все прочее некорректное поведение для этого состояния
@admin_router.message(AddProduct.image)
async def add_image2(message: types.Message, state: FSMContext):
    await message.answer("Отправьте фото.")


################# Микро FSM для загрузки/изменения баннеров ############################

class AddBanner(StatesGroup):
    image = State()

# Отправляем перечень информационных страниц бота и становимся в состояние отправки photo
@admin_router.callback_query(StateFilter(None), F.data == 'add_change_banner')
async def add_image2(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):
    pages_names = [page.name for page in await orm_get_info_pages(session)]
    await callback.message.answer(f"Отправьте фото баннера.\nВ описании укажите для какой страницы:\
                         \n{', '.join(pages_names)}")
    await state.set_state(AddBanner.image)

# Добавляем/изменяем изображение в таблице (там уже есть записанные страницы по именам:
# main, catalog, cart(для пустой корзины), about, payment, shipping
@admin_router.message(AddBanner.image, F.photo)
async def add_banner(message: types.Message, state: FSMContext, session: AsyncSession):
    image_id = message.photo[-1].file_id
    for_page = message.caption.strip()
    pages_names = [page.name for page in await orm_get_info_pages(session)]
    if for_page not in pages_names:
        await message.answer(f"Введите нормальное название страницы, например:\
                         \n{', '.join(pages_names)}")
        return
    await orm_change_banner_image(session, for_page, image_id,)
    await message.answer("Баннер добавлен/изменен.")
    await state.clear()

# ловим некоррекный ввод
@admin_router.message(AddBanner.image)
async def add_banner2(message: types.Message, state: FSMContext):
    await message.answer("Отправьте фото баннера или отмена")

#######################################################################################


# Вернутся на шаг назад (на прошлое состояние)
# Прописано для двух машин состояний: из make_offer и add_product
@admin_router.message(StateFilter("*"), Command("назад"))
@admin_router.message(StateFilter("*"), F.text.casefold() == "назад")
async def back_step_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()

    if current_state in (AddProduct.name, AddOffer.name, Add_FAQ.name, Add_price.name, Add_document.name, AddNote.name):
        await message.answer(
            'Предидущего шага нет, или введите название или напишите "отмена"'
        )
        return

    elif current_state == AddNote.description:
        await state.set_state(AddNote.name)
        await message.answer(
            f"Ок, вы вернулись к прошлому шагу \n {AddNote.texts[AddNote.name]}"
        )
        return

    elif current_state == Add_price.price:
        await state.set_state(Add_price.name)
        await message.answer(
            f"Ок, вы вернулись к прошлому шагу \n {Add_price.texts[Add_price.name]}"
        )
        return

    elif current_state == Add_document.document:
        await state.set_state(Add_document.name)
        await message.answer(
            f"Ок, вы вернулись к прошлому шагу \n {Add_document.texts[Add_document.name]}"
        )
        return

    elif current_state == AddOffer.description:
        await state.set_state(AddOffer.name)
        await message.answer(
            f"Ок, вы вернулись к прошлому шагу \n {AddOffer.texts[AddOffer.name]}"
        )
        return

    elif current_state == AddOffer.making_offer or current_state == AddOffer.discount:
        await state.set_state(AddOffer.description)
        await message.answer(
            f"Ок, вы вернулись к прошлому шагу \n {AddOffer.texts[AddOffer.description]}"
        )
        return


    elif current_state == AddProduct.price:
        await state.set_state(AddProduct.description)
        await message.answer(
            f"Ок, вы вернулись к прошлому шагу \n {AddProduct.texts[AddProduct.description]}"
        )
        return


    elif current_state == Add_FAQ.description:
        await state.set_state(Add_FAQ.name)
        await message.answer(
            f"Ок, вы вернулись к прошлому шагу \n {Add_FAQ.texts[Add_FAQ.name]}"
        )
        return


    previous = None
    for step in AddProduct.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(
                f"Ок, вы вернулись к прошлому шагу \n {AddProduct.texts[previous.state]}"
            )
            return
        previous = step


@admin_router.callback_query(F.data == 'tables_links')
async def get_tables_links(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/list_links_work_tables'], disable_web_page_preview=True,
                                  reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)) )
    await callback.message.delete()


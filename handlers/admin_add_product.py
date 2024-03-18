from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession

from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_add_product import inline_product_add_dell_kb
from filters.is_admin import IsAdminMsg
from database.orm_query import orm_add_product, orm_get_products, orm_delete_product, \
    orm_update_product, orm_get_product
from keyboards.inline.inline_add_product import get_callback_btns

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



@admin_router.message(Command("admin"), F.text| F.command)
@admin_router.callback_query(lambda c: c.data.startswith("admin"))
async def admin_handler(message_or_callback: types.Union[types.Message, CallbackQuery]):
    if isinstance(message_or_callback, types.Message):
        # Если это сообщение
        message = message_or_callback
        await message.answer(text="Добавте товар👇", reply_markup=inline_product_add_dell_kb)
    elif isinstance(message_or_callback, CallbackQuery):
        # Если это колбэк-запрос
        callback_query = message_or_callback
        await callback_query.message.answer(text="Добавте товар👇", reply_markup=inline_product_add_dell_kb)


@admin_router.callback_query(F.data == 'all_products_list')
async def product_list_all(callback: types.CallbackQuery, session: AsyncSession):
    for product in await orm_get_products(session):
        await callback.message.answer_photo(
            product.image,
            caption=f"<strong>{product.name}</strong>\n"
                    f"{product.description}\n"
                    f"Стоимость: {round(product.price, 2)}",
            reply_markup=get_callback_btns(btns={
                'Удалить': f"delete_{product.id}",
                'Изменить': f"change_{product.id}",
            })
        )
    await callback.message.answer("Ок, вот список предложений.")


@admin_router.callback_query(StateFilter(None), F.data.startswith('change_'))
async def change_product(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):

    product_id = callback.data.split("_")[-1]
    product_for_change = await orm_get_product(session, int(product_id))

    AddProduct.product_for_change = product_for_change

    await callback.answer()
    await callback.message.answer("Введите название товара")
    await state.set_state(AddProduct.name)


@admin_router.callback_query(F.data.startswith('delete_'))
async def delete_product(callback: types.CallbackQuery, session: AsyncSession):

    product_id = callback.data.split("_")[-1]
    await orm_delete_product(session, int(product_id))

    await callback.answer('Предложение удалено.')
    await callback.message.answer('Предложение удалено.')


# Код ниже для машины состояний (FSM)

@admin_router.callback_query(StateFilter(None), F.data == 'add_product')
# Становимся в состояние ожидания ввода name
async def add_product(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название товара")
    await callback.message.delete()
    await state.set_state(AddProduct.name)


# Хендлер отмены и сброса состояния должен быть всегда именно хдесь,
# после того как только встали в состояние номер 1 (элементарная очередность фильтров)
@admin_router.message(StateFilter('*'), Command("отмена"))
@admin_router.message(StateFilter('*'), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    if AddProduct.product_for_change:
        AddProduct.product_for_change = None
    await state.clear()
    await message.answer("Действия отменены", reply_markup=inline_product_add_dell_kb)


# Вернутся на шаг назад (на прошлое состояние)
@admin_router.message(StateFilter('*'), Command("назад"))
@admin_router.message(StateFilter('*'), F.text.casefold() == "назад")
async def back_step_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()

    if current_state == AddProduct.name:
        await message.answer('Предидущего шага нет, или введите название товара или напишите "отмена"')
        return

    previous = None
    for step in AddProduct.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f"Ок, вы вернулись к прошлому шагу \n {AddProduct.texts[previous.state]}")
            return
        previous = step


# Ловим данные для состояние name и потом меняем состояние на description
@admin_router.message(AddProduct.name, or_f(F.text, F.text == "."))
async def add_name(message: types.Message, state: FSMContext):
    if message.text == ".":
        await state.update_data(name=AddProduct.product_for_change.name)
    else:
        # Здесь можно сделать какую либо дополнительную проверку
        # и выйти из хендлера не меняя состояние с отправкой соответствующего сообщения
        # например:
        if len(message.text) >= 100:
            await message.answer("Название товара не должно превышать 100 символов. \n Введите заново")
            return

        await state.update_data(name=message.text)
    await message.answer("Введите описание товара")
    await state.set_state(AddProduct.description)


# Хендлер для отлова некорректных вводов для состояния name
@admin_router.message(AddProduct.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст названия товара")


# Ловим данные для состояние description и потом меняем состояние на price
@admin_router.message(AddProduct.description, or_f(F.text, F.text == "."))
async def add_description(message: types.Message, state: FSMContext):
    if message.text == ".":
        await state.update_data(description=AddProduct.product_for_change.description)
    else:
        await state.update_data(description=message.text)
    await message.answer("Введите стоимость товара")
    await state.set_state(AddProduct.price)


# Хендлер для отлова некорректных вводов для состояния description
@admin_router.message(AddProduct.description)
async def add_description2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст описания товара")


# Ловим данные для состояние price и потом меняем состояние на image
@admin_router.message(AddProduct.price, or_f(F.text, F.text == "."))
async def add_price(message: types.Message, state: FSMContext):
    if message.text == ".":
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
# В любом из обработчиков мы можем обраиться к session, т.к. передали сессию в main функцию.
@admin_router.message(AddProduct.image, or_f(F.photo, F.text == '.'))
async def add_image(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text == ".":
        await state.update_data(image=AddProduct.product_for_change.image)
    else:
        await state.update_data(image=message.photo[-1].file_id)

    data = await state.get_data()
    try:
        if AddProduct.product_for_change:
            await orm_update_product(session, AddProduct.product_for_change.id, data)
            await message.answer("Предложение изменено.", reply_markup=inline_product_add_dell_kb)
        else:
            await orm_add_product(session, data)
            await message.answer("Предложение добавлено.", reply_markup=inline_product_add_dell_kb)
        await state.clear()

    except Exception as e:
        await message.answer(
            f"Ошибка: \n{str(e)}\nОбратись к прогеру. Имей в виду, что это не бесплатно.", reply_markup=inline_product_add_dell_kb
        )
    AddProduct.product_for_change = None


@admin_router.message(AddProduct.image)
async def add_image2(message: types.Message, state: FSMContext):
    await message.answer("Отправьте фото пищи")

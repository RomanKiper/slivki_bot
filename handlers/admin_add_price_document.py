from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession
from filters.chat_types import ChatTypeFilter
from filters.is_admin import IsAdminMsg
from database.orm_query import orm_add_price, orm_get_prices, orm_delete_price, orm_add_document, orm_delete_document, \
    orm_get_documents
from keyboards.inline.inline_add_product import get_callback_btns, get_inlineMix_btns
from lexicon.lexicon import LEXICON_btn_main_admin_menu, LEXICON_btn_back_menu_links

admin_add_document_price_router = Router()
admin_add_document_price_router.message.filter(ChatTypeFilter(['private']), IsAdminMsg())
admin_add_document_price_router.callback_query.filter(IsAdminMsg())


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


@admin_add_document_price_router.callback_query(F.data == 'price_list')
async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
    price_file = await orm_get_prices(session)
    if len(price_file) > 0:
        for pr in price_file:
            await callback.message.answer_document(document=pr.price, caption=f"{pr.name}", reply_markup=get_callback_btns(
                btns={
                    "Удалить": f"price_del_{pr.id}",
                    "Админка": f"admin",
                },
                sizes=(2,)
            ))
    else:
        await callback.message.answer(
            "У вас нет добавленных прайсов.🤔\nДобавьте прайсы через администартивную панель.📝")



@admin_add_document_price_router.callback_query(F.data == 'valable_prices_list')
async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
    price_file = await orm_get_prices(session)
    for pr in price_file:
        await callback.message.answer_document(document=pr.price, caption=f"{pr.name}",
                                               reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)))


@admin_add_document_price_router.callback_query(F.data.startswith("price_del_"))
async def delete_product_callback(callback: types.CallbackQuery, session: AsyncSession):
    product_id = callback.data.split("_")[-1]
    await orm_delete_price(session, int(product_id))
    await callback.answer("Прайс удален")
    await callback.message.answer("Прайс удален!")

# FSM:
# Становимся в состояние ожидания ввода name
@admin_add_document_price_router.callback_query(StateFilter(None), F.data == 'add_price')
# Становимся в состояние ожидания ввода name
async def add_product(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название прайса или комментарий к прайсу.")
    await callback.message.delete()
    await state.set_state(Add_price.name)


# Хендлер отмены и сброса состояния должен быть всегда именно хдесь,
# после того как только встали в состояние номер 1 (элементарная очередность фильтров)


# Ловим данные для состояние name и потом меняем состояние на price
@admin_add_document_price_router.message(Add_price.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if 4 >= len(message.text) >= 150:
        await message.answer(
            "Название прайса не должно превышать 150 символов\nили быть менее 5ти символов. \n Введите заново"
        )
        return
    await state.update_data(name=message.text)
    await message.answer("Загрузите прайс")
    await state.set_state(Add_price.price)

# Хендлер для отлова некорректных вводов для состояния name
@admin_add_document_price_router.message(Add_price.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите название прайса!")


# Ловим данные для состояние price и потом выходим из состояний
@admin_add_document_price_router.message(Add_price.price, F.document)
async def add_document(message: types.Message, state: FSMContext, session: AsyncSession):

    if message.document:
        await state.update_data(price=message.document.file_id)
    else:
        await message.answer("Загрузите документ в правильном формате!")
        return
    data = await state.get_data()
    try:
        await orm_add_price(session, data)
        await message.answer("Прайс добавлен", reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))
        await state.clear()

    except Exception as e:
        await message.answer(
            f"Ошибка: \n{str(e)}\nОбратись к программеру, он опять денег хочет",
            reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)),
        )
        await state.clear()


# Ловим все прочее некорректное поведение для этого состояния
@admin_add_document_price_router.message(Add_price.price)
async def add_image2(message: types.Message, state: FSMContext):
    await message.answer("Загрузите файл.")


#################################### Обработчики документов ######################################


@admin_add_document_price_router.callback_query(F.data == 'documents_list')
async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
    document_file = await orm_get_documents(session)
    if len(document_file) > 0:
        for dc in document_file:
            await callback.message.answer_document(document=dc.document, caption=f"{dc.name}", reply_markup=get_callback_btns(
                btns={
                    "Удалить": f"document_del_{dc.id}",
                    "Админка": f"admin",
                },
                sizes=(2,)
            ))
    else:
        await callback.message.answer(
            "У вас нет добавленных документов.🤔\nДобавьте документы через администартивную панель.📝")


@admin_add_document_price_router.callback_query(F.data == 'presentations_list')
async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
    document_file = await orm_get_documents(session)
    if len(document_file) > 0:
        for dc in document_file:
            await callback.message.answer_document(document=dc.document, caption=f"{dc.name}", reply_markup=get_inlineMix_btns(btns=LEXICON_btn_back_menu_links, sizes=(1,)))
    else:
        await callback.message.answer(
            "У вас нет добавленных документов.🤔\nДобавьте документы через администартивную панель.📝")


@admin_add_document_price_router.callback_query(F.data.startswith("document_del_"))
async def delete_product_callback(callback: types.CallbackQuery, session: AsyncSession):
    product_id = callback.data.split("_")[-1]
    await orm_delete_document(session, int(product_id))
    await callback.answer("Документ удален")
    await callback.message.answer("Документ удален!")

# FSM:
# Становимся в состояние ожидания ввода name
@admin_add_document_price_router.callback_query(StateFilter(None), F.data == 'add_docoment')
# Становимся в состояние ожидания ввода name
async def add_product(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название документа или комментарий к документу.")
    await callback.message.delete()
    await state.set_state(Add_document.name)


# Хендлер отмены и сброса состояния должен быть всегда именно хдесь,
# после того как только встали в состояние номер 1 (элементарная очередность фильтров)


# Ловим данные для состояние name и потом меняем состояние на document
@admin_add_document_price_router.message(Add_document.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if 4 >= len(message.text) >= 150:
        await message.answer(
            "Название документа не должно превышать 150 символов\nили быть менее 5ти символов. \n Введите заново"
        )
        return
    await state.update_data(name=message.text)
    await message.answer("Загрузите документ")
    await state.set_state(Add_document.document)

# Хендлер для отлова некорректных вводов для состояния name
@admin_add_document_price_router.message(Add_document.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите название документа!")


# Ловим данные для состояние document и потом выходим из состояний
@admin_add_document_price_router.message(Add_document.document, F.document)
async def add_document(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.document:
        await state.update_data(document=message.document.file_id)
    else:
        await message.answer("Загрузите документ в правильном формате!")
        return
    data = await state.get_data()
    try:
        await orm_add_document(session, data)
        await message.answer("Документ добавлен", reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))
        await state.clear()

    except Exception as e:
        await message.answer(
            f"Ошибка: \n{str(e)}\nОбратись к программеру, он опять денег хочет",
            reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)),
        )
        await state.clear()


# Ловим все прочее некорректное поведение для этого состояния
@admin_add_document_price_router.message(Add_document.document)
async def add_image2(message: types.Message, state: FSMContext):
    await message.answer("Загрузите файл.")
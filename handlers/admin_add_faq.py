from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession

from filters.chat_types import ChatTypeFilter
from filters.is_admin import IsAdminMsg
from database.orm_query import orm_delete_faq, orm_get_faq,  orm_add_faq, orm_get_faqs
from keyboards.inline.inline_add_product import get_callback_btns
from lexicon.lexicon import LEXICON_btn_main_admin_menu

admin_faq_router = Router()
admin_faq_router.message.filter(ChatTypeFilter(['private']), IsAdminMsg())
admin_faq_router.callback_query.filter(IsAdminMsg())


class Add_FAQ(StatesGroup):
    # Шаги состояний
    name = State()
    description = State()

    texts = {
        'AddProduct:name': 'Введите название заново:',
        'AddProduct:description': 'Введите описание заново:',
    }



@admin_faq_router.callback_query(F.data == 'faq_list')
async def admin_features(callback: types.CallbackQuery, session: AsyncSession):
    faqs = await orm_get_faqs(session)
    btns = {faq.name: f'faq_{faq.id}' for faq in faqs}
    await callback.message.answer("Часто задаваемые вопросы:", reply_markup=get_callback_btns(btns=btns))


@admin_faq_router.callback_query(F.data.startswith('faq_'))
async def starring_at_product(callback: types.CallbackQuery, session: AsyncSession):
    faq_id = callback.data.split('_')[-1]
    faq_item = await orm_get_faq(session, int(faq_id))
    await callback.message.answer(
        f"<strong>{faq_item.name}</strong>\n\n"
        f"{faq_item.description}\n\n",
        reply_markup=get_callback_btns(
            btns={
                "Удалить": f"drop_{faq_item.id}",
                "Назад": f"faq_list",
            },
            sizes=(2,)
        ),
    )
    await callback.answer()




@admin_faq_router.callback_query(F.data.startswith("drop_"))
async def delete_product_callback(callback: types.CallbackQuery, session: AsyncSession):
    product_id = callback.data.split("_")[-1]
    await orm_delete_faq(session, int(product_id))

    await callback.answer("Вопрос удален")
    await callback.message.answer("Вопрос удален!")

# FSM:

# Становимся в состояние ожидания ввода name
@admin_faq_router.callback_query(StateFilter(None), F.data == 'add_faq')
# Становимся в состояние ожидания ввода name
async def add_product(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название часто задаваемого вопроса")
    await callback.message.delete()
    await state.set_state(Add_FAQ.name)


# Хендлер отмены и сброса состояния должен быть всегда именно хдесь,
# после того как только встали в состояние номер 1 (элементарная очередность фильтров)


# Вернутся на шаг назад (на прошлое состояние)
# Прописано для двух машин состояний: из make_offer и add_product
# @admin_router.message(StateFilter("*"), Command("назад"))
# @admin_router.message(StateFilter("*"), F.text.casefold() == "назад")
# async def back_step_handler(message: types.Message, state: FSMContext) -> None:
#     current_state = await state.get_state()
#
#     if current_state == AddProduct.name or current_state == AddOffer.name:
#         await message.answer(
#             'Предидущего шага нет, или введите название или напишите "отмена"'
#         )
#         return
#
#     elif current_state == AddOffer.description:
#         await state.set_state(AddOffer.name)
#         await message.answer(
#             f"Ок, вы вернулись к прошлому шагу \n {AddOffer.texts[AddOffer.name]}"
#         )
#         return
#
#     elif current_state == AddOffer.making_offer or current_state == AddOffer.discount:
#         await state.set_state(AddOffer.description)
#         await message.answer(
#             f"Ок, вы вернулись к прошлому шагу \n {AddOffer.texts[AddOffer.description]}"
#         )
#         return
#
#
#     elif current_state == AddProduct.price:
#         await state.set_state(AddProduct.description)
#         await message.answer(
#             f"Ок, вы вернулись к прошлому шагу \n {AddProduct.texts[AddProduct.description]}"
#         )
#         return
#
#     previous = None
#     for step in AddProduct.__all_states__:
#         if step.state == current_state:
#             await state.set_state(previous)
#             await message.answer(
#                 f"Ок, вы вернулись к прошлому шагу \n {AddProduct.texts[previous.state]}"
#             )
#             return
#         previous = step


# Ловим данные для состояние name и потом меняем состояние на description
@admin_faq_router.message(Add_FAQ.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if 4 >= len(message.text) >= 150:
        await message.answer(
            "Название товара не должно превышать 150 символов\nили быть менее 5ти символов. \n Введите заново"
        )
        return

    await state.update_data(name=message.text)

    await message.answer("Введите описание товара")
    await state.set_state(Add_FAQ.description)

# Хендлер для отлова некорректных вводов для состояния name
@admin_faq_router.message(Add_FAQ.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст названия часто задаваемого вопроса!")


# Ловим данные для состояние description
@admin_faq_router.message(Add_FAQ.description, F.text)
async def add_description(message: types.Message, state: FSMContext, session: AsyncSession):
    if 4 >= len(message.text):
        await message.answer(
            "Слишком короткое описание. \n Введите заново"
        )
        return
    await state.update_data(description=message.text)
    data = await state.get_data()

    try:
        await orm_add_faq(session, data)
        await message.answer("Вопрос добавлен", reply_markup=get_callback_btns(btns=LEXICON_btn_main_admin_menu, sizes=(2,)))
        await state.clear()

    except Exception as e:
        await message.answer(
            f"Ошибка: \n{str(e)}\nОбратись к программеру, он опять денег хочет", sizes=(2,))
        await state.clear()


# Хендлер для отлова некорректных вводов для состояния description
@admin_faq_router.message(Add_FAQ.description)
async def add_description2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст часто задаваемого вопроса")


from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_add_advert import inline_product_add_dell_kb
from filters.is_admin import IsAdminMsg

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdminMsg())
admin_router.callback_query.filter(IsAdminMsg())


@admin_router.message(Command("admin"), F.text| F.command)
@admin_router.callback_query(lambda c: c.data.startswith("admin"))
async def admin_handler(message_or_callback: types.Union[types.Message, CallbackQuery]):
    if isinstance(message_or_callback, types.Message):
        # Если это сообщение
        message = message_or_callback
        await message.answer(text="👇👇Добавте товар👇👇", reply_markup=inline_product_add_dell_kb)
    elif isinstance(message_or_callback, CallbackQuery):
        # Если это колбэк-запрос
        callback_query = message_or_callback
        await callback_query.message.answer(text="👇👇Добавте товар👇👇", reply_markup=inline_product_add_dell_kb)


class AddProduct(StatesGroup):
    name = State()
    description = State()
    price = State()
    image = State()

@admin_router.callback_query(StateFilter(None), F.data == 'add_product')
async def inline_add_product_start(message: types.Message, state: FSMContext):
    await message.answer(text="Введите название нового предложения:")
    await state.set_state(AddProduct.name)

@admin_router.message(Command('cancel'))
@admin_router.message(F.text.casefold() == 'cancel')
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(text='Действия отменены', reply_markup=inline_product_add_dell_kb)

@admin_router.message(Command('back'))
@admin_router.message(F.text.casefold() == 'back')
async def back_step_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(f'Вы вернулись к прошлому шагу.')


@admin_router.message(AddProduct.name, F.text)
async def inline_add_product_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="Введите описание предложения:")
    await state.set_state(AddProduct.description)

@admin_router.message(AddProduct.description, F.text)
async def inline_add_product_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer(text="Введите стоимость предложения:")
    await state.set_state(AddProduct.price)

@admin_router.message(AddProduct.price, F.text)
async def inline_add_product_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(text="Загрузите изображение предложения:")
    await state.set_state(AddProduct.image)

@admin_router.message(AddProduct.image, F.photo)
async def inline_add_image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    await message.answer(text="Предложение добавлено.", reply_markup=inline_product_add_dell_kb)
    data = await state.get_data()
    print(data)
    # await message.answer(str(data))
    # await state.clear()





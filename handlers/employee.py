from aiogram import Router, types, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
from config_data.config import load_config, Config
from filters.chat_types import ChatTypeFilter
from keyboards.inline.inline_employee_menu import create_inline_kb_employee_meny
from filters.is_admin import IsAdminMsg

employee_router = Router()
employee_router.message.filter(ChatTypeFilter(['private']), IsAdminMsg())

config: Config = load_config()
lst_admin_ids = config.tg_bot.id_admins


@employee_router.message(F.text.lower().in_({'работникам', 'сотрудникам', "employee"}))
@employee_router.message(Command('employee'))
async def get_main_menu(message: Message):
    # if message.from_user.id in lst_admin_ids:
    keyboard = create_inline_kb_employee_meny(1, 'tables_links', 'work_links', 'offer_online', 'add_advertising')

    await message.answer(
        text='У вас права работника компании.'
             ' Пользуйтесь возможнстями бота и пишите ваши рекомендации по усовершенствованию бота.',
        reply_markup=keyboard
    )
    await message.delete()
    # else:
    #     await message.answer(text="Нет прав доступа. Запросите права у администатора.")
    #     await message.delete()




#
# @router.callback_query(F.data=='employee')
# async def get_main_menu_2(callback: types.CallbackQuery):
#     # if callback.from_user.id in lst_admin_ids:
#         await callback.message.answer(
#             text='У вас права работника компании.'
#                  ' Пользуйтесь возможнстями бота и пишите ваши рекомендации по усовершенствованию бота.',
#             reply_markup=inline_kb_employee
#         )
#         await callback.message.delete()
#     # else:
#     #     await callback.message.answer(text="Нет прав доступа. Запросите права у администатора.")
#     #     await callback.message.delete()
#
#
#
# @router.callback_query(F.data == 'school')
# async def get_school_document(callback: types.CallbackQuery):
#     await callback.message.answer(
#         text='Данный раздел находится в разработке.'
#     )
#
#
# @router.callback_query(F.data == 'improvements')
# async def get_improvements(callback: types.CallbackQuery):
#     await callback.message.answer(
#         text='Данный раздел находится в разработке.'
#     )
from aiogram.filters import Filter
from aiogram import types, Bot
from config_data.config import Config, load_config

config: Config = load_config()

class IsAdminMsg(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message) -> bool:
        if message.from_user.id in config.tg_bot.id_admins:
            return True
        else:
            await message.answer(text="Нет прав")


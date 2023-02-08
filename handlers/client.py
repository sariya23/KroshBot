from aiogram import types, Dispatcher
from create_bot import bot, dp


async def empty(message: types.Message):
    await bot.send_message(f'Я кролик-бот и реагирую только на определенные команды, прям как настоящий кролик')

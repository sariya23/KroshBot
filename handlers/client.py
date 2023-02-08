from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards.client_kb import client_keyboard_start


async def empty(message: types.Message):
    """An empty handler does not work on commands"""
    await bot.send_message(message.from_user.id,
                           f'Я кролик-бот и реагирую только на определенные команды, прям как настоящий кролик',
                           reply_markup=client_keyboard_start)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(empty)

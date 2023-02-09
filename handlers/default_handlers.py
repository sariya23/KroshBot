from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text
from keyboards.inline.inline_start import client_keyboard_start
from keyboards.inline.inline_commands import client_keyboard_commands


async def start(mesesage: types.Message):
    await bot.send_message(mesesage.from_user.id,
                           'Я кролик-бот. Меня зовут Крош. Я реагирую только'
                           ' на определенные команды.',
                           reply_markup=client_keyboard_start)


async def commands(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Вот что я умею',
                           reply_markup=client_keyboard_commands)


def register_default_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=('start'))
    dp.register_message_handler(commands, commands=('commands'))

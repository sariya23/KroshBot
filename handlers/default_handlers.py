from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text
from keyboards.inline.inline_start import client_keyboard_start


async def start(mesesage: types.Message):
    await bot.send_message(mesesage.from_user.id,
                           'Я кролик-бот. Меня зовут Крош. Я реагирую только'
                           ' на определенные команды.',
                           reply_markup=client_keyboard_start)


def register_default_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=('start'))

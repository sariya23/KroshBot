from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.inline.inline_start import client_keyboard_start
from keyboards.inline.inline_commands import client_keyboard_commands
from keyboards.inline.inline_breeds import client_keyboard_breeds


async def start(mesesage: types.Message):
    """Triggers by command /start"""
    await bot.send_message(mesesage.from_user.id,
                           'Я кролик-бот. Меня зовут Крош. Я реагирую только'
                           ' на определенные команды.',
                           reply_markup=client_keyboard_start)


async def commands(message: types.Message):
    """Triggers by command /commands"""
    await bot.send_message(message.from_user.id,
                           'Вот что я умею',
                           reply_markup=client_keyboard_commands)


async def phone(message: types.Message):
    """Triggers by command /phone"""
    await bot.send_message(message.from_user.id,
                           'Звони сюда: \n'
                           '+79252215934')


async def email(message: types.Message):
    """Triggers by command /email"""
    await bot.send_message(message.from_user.id,
                           'Пиши сюда:\ntsarskiy_krolik@mail.ru')


async def rabbits_breeds(message: types.Message):
    """Triggers by command /rabbits"""
    await bot.send_message(message.from_user.id,
                           'Нас много, но мы разные',
                           reply_markup=client_keyboard_breeds)


def register_default_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=('start'))
    dp.register_message_handler(commands, commands=('commands'))
    dp.register_message_handler(phone, commands=('phone'))
    dp.register_message_handler(email, commands=('email'))
    dp.register_message_handler(rabbits_breeds, commands=('rabbits'))

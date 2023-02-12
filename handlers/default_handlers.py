from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import bot
from keyboards.inline.inline_start import client_keyboard_start
from keyboards.inline.inline_commands import client_keyboard_commands
from keyboards.inline.inline_breeds import client_keyboard_breeds


async def start(message: types.Message):
    """Triggers by command /start"""
    await bot.send_message(message.from_user.id,
                           f'Привет 👋, <b>{message.from_user.first_name}</b>\n\n'
                           f'Я <b>Кролик</b>🐰, который живет внутри Телеграма 😀\n'
                           f'К сожалению, кролики в реальной жизни не разговаривают, '
                           f'но все понимают.\n\n'
                           f'Я - кролик особенный - я и понимаю, и разговариваю, поэтому буду их общим голосом🔊\n\n'
                           f'Я помогу тебе, чем смогу☺.',
                           reply_markup=client_keyboard_start,
                           parse_mode='HTML')


async def help_(message: types.Message):
    """Triggers by command /help"""
    await bot.send_message(message.from_user.id,
                           f'Кролик-бот помогает человеку... Дожили\n'
                           f'Через меня мы можешь узнать:\n'
                           f'🔴Адрес\n'
                           f'🔴Телефон\n'
                           f'🔴Электронную почту\n'
                           f'🔴Множество пород кроликов\n'
                           )


async def commands(message: types.Message):
    """Triggers by command /commands"""
    await bot.send_message(message.from_user.id,
                           'Вот что я умею',
                           reply_markup=client_keyboard_commands)


async def rabbits_breeds(message: types.Message):
    """Triggers by command /rabbits"""
    await bot.send_message(message.from_user.id,
                           'Нас много, но мы разные',
                           reply_markup=client_keyboard_breeds)


# async def test_edit(message: types.Message):
#     await bot.send_photo(
#         message.from_user.id,
#         'https://avatars.mds.yandex.net/i?id=a707b920e4b006e4c9dfcd6cf9e121d79191634c-7764851-images-thumbs&n=13',
#         'text1',
#         reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('next', callback_data='next'))
#     )


def register_default_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=('start'))
    dp.register_message_handler(help_, commands=('help'))
    dp.register_message_handler(commands, commands=('commands'))
    dp.register_message_handler(rabbits_breeds, commands=('rabbits'))
    # dp.register_message_handler(test_edit, commands=('test'))
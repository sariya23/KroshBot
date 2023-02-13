from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

from create_bot import bot
from aiogram.dispatcher.filters import Text

from keyboards.inline.inline_breeds import client_keyboard_breeds
from keyboards.inline.inline_commands import client_keyboard_commands

from utils.Parser_class import Parser

import time

english_to_russian = {
    'belichij': 'Беличий карлик',
    'germelin': 'Гермелин',
    'karlikovyj-baran': 'Карликовый барон',
    'minor': 'Менор',
    'minilop': 'МиниЛоп',
    'niderlandskij': 'Нидерландский',
    'xotot': 'Хотот',
    'cvetnoj-karlik': 'Цветной карлик'
}


async def empty(message: types.Message):
    """An empty handler does not work on commands"""
    await bot.send_message(message.from_user.id,
                           f'Неизвестная команда(. Чтобы увидеть мои возможности '
                           f'пропиши /commands', )


async def command_start(callback: types.CallbackQuery):
    """Triggers by command /start
    Send inline keyboards with commands"""
    await bot.send_message(callback.from_user.id,
                           f'Меня запрограммировали на следующие команды:',
                           reply_markup=client_keyboard_commands,
                           parse_mode='HTML')
    await callback.answer()


async def send_address_shop(callback: types.CallbackQuery):
    """Send address of the shop"""
    await bot.send_message(callback.from_user.id,
                           '📌Мы с братьями и сестрами тусуемся здесь:\n'
                           '<b>Московская область Деревня Тарычево, ул. Яблоневая 7-В</b>',
                           parse_mode='HTML')
    await callback.answer()


async def send_phone_number(callback: types.CallbackQuery):
    """Send phone number"""
    await bot.send_message(callback.from_user.id, '☎Звони сюда:\n'
                                                  '+79252215934')
    await callback.answer()


async def send_email_address(callback: types.CallbackQuery):
    """Send email address"""
    await bot.send_message(callback.from_user.id, '📮Пиши сюда:\ntsarskiy_krolik@mail.ru')
    await callback.answer()


async def show_catalog(callback: types.CallbackQuery):
    """Send inline keyboard with breeds of the rabbits"""
    await bot.send_message(callback.from_user.id,
                           'Нас много, но все мы разные',
                           reply_markup=client_keyboard_breeds)
    await callback.answer()


async def next_call(call: types.CallbackQuery):
    amount_rabbits = int(call.data.split()[3])  # amount rabbits to the end of the list
    i = int(call.data.split()[1])  # pos of the current rabbit in th list
    breed = call.data.split()[2]  # current breed
    start_time = time.monotonic()
    data = Parser().parse(breed)[i]
    end_time = time.monotonic()
    print(end_time - start_time)
    is_sale = bool(data.discount_price)
    price_message = f"💵Стоимость по скидке💵: " if is_sale else "💵Стоимость счастья💵: "
    price_value = f"{data.discount_price}" if is_sale else f"{data.old_price}"
    end_to_sale = f"<b>⌛СКИДКА ПРОДЛИТСЯ ЕЩЕ⌛</b>: {data.time_to_disc_end}\n" if is_sale else ""

    await bot.edit_message_media(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        media=InputMediaPhoto(media=data.img_url)

    )

    if amount_rabbits > 1:
        await bot.edit_message_caption(
            caption=f'🐇Пушистик породы🐇: <b>{data.breed}</b>\n'
                    f'{price_message}'
                    f'{price_value}\n'
                    f'{end_to_sale}'
                    f'🔬Подробнее🔬: {data.more_info}',

            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton('◀ Предыдущий',
                                     callback_data=f'back {i - 1} {breed} {amount_rabbits + 1}')).insert(
                InlineKeyboardButton('Следующий ▶', callback_data=f'next {i + 1} {breed} {amount_rabbits - 1}')),
            parse_mode='HTML'
        )
    else:
        await bot.edit_message_caption(
            caption=f'🐇Пушистик породы🐇: <b>{data.breed}</b>\n'
                    f'{price_message}'
                    f'{price_value}\n'
                    f'{end_to_sale}'
                    f'🔬Подробнее🔬: {data.more_info}',

            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton('Предыдущий ◀', callback_data=f'back {i - 1} {breed} {amount_rabbits + 1}')),
            parse_mode='HTML'
        )
        await call.answer()


async def back_call(call: types.CallbackQuery):
    _, i, breed, amount_rabbits = call.data.split()
    i = int(i)
    amount_rabbits = int(amount_rabbits)
    data = Parser().parse(breed)[i]
    is_sale = bool(data.discount_price)
    price_message = f"💵Стоимость по скидке💵: " if is_sale else "💵Стоимость счастья💵: "
    price_value = f"{data.discount_price}" if is_sale else f"{data.old_price}"
    end_to_sale = f"<b>⌛СКИДКА ПРОДЛИТСЯ ЕЩЕ⌛</b>: {data.time_to_disc_end}\n" if is_sale else ""

    await bot.edit_message_media(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        media=InputMediaPhoto(media=data.img_url)

    )

    if i == 0:
        await bot.edit_message_caption(
            caption=f'🐇Пушистик породы🐇: <b>{data.breed}</b>\n'
                    f'{price_message}'
                    f'{price_value}\n'
                    f'{end_to_sale}'
                    f'🔬Подробнее🔬: {data.more_info}',

            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=InlineKeyboardMarkup().insert(
                InlineKeyboardButton('Следующий ▶', callback_data=f'next {i + 1} {breed} {amount_rabbits - 1}')),
            parse_mode='HTML'
        )
    else:
        await bot.edit_message_caption(
            caption=f'🐇Пушистик породы🐇: <b>{data.breed}</b>\n'
                    f'{price_message}'
                    f'{price_value}\n'
                    f'{end_to_sale}'
                    f'🔬Подробнее🔬: {data.more_info}',
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton('◀ Предыдущий',
                                     callback_data=f'back {i - 1} {breed} {amount_rabbits + 1}')).insert(
                InlineKeyboardButton('Следующий ▶', callback_data=f'next {i + 1} {breed} {amount_rabbits - 1}')),
            parse_mode='HTML'
        )

    await call.answer()


async def show_picked_breed(call: types.CallbackQuery):
    """Send first rabbit of picked breed
    Callback_data:
    :next - flag that button next
    :1 - pos of next rabbit
    :breed - current breed for next parse
    :amount_rabbits - 1 counter that count how any rabbit lost to the end"""
    breed = call.data.split()[1]
    url = Parser.get_url(breed)
    start_time = time.monotonic()
    data = Parser().parse(breed)
    end_time = time.monotonic()
    print(end_time - start_time)
    amount_rabbits = len(data)

    is_sale = bool(data[0].discount_price)
    price_message = f"💵Стоимость по скидке💵: " if is_sale else "💵Стоимость счастья💵: "
    price_value = f"{data[0].discount_price}" if is_sale else f"{data[0].old_price}"
    end_to_sale = f"<b>⌛СКИДКА ПРОДЛИТСЯ ЕЩЕ⌛</b>: {data[0].time_to_disc_end}\n" if is_sale else ""

    if amount_rabbits > 1:
        await bot.send_photo(call.from_user.id, data[0].img_url,
                             f'🐇Пушистик породы🐇: <b>{data[0].breed}</b>\n'
                             f'{price_message}'
                             f'{price_value}\n'
                             f'{end_to_sale}'
                             f'🔬Подробнее🔬: {data[0].more_info}',
                             parse_mode='html',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton('Следующий ▶',
                                                      callback_data=f'next 1 {breed} {amount_rabbits - 1}')))
    else:
        await bot.send_photo(call.from_user.id, data[0].img_url,
                             f'🐇Пушистик породы🐇: <b>{data[0].breed}</b>\n'
                             f'{price_message}'
                             f'{price_value}\n'
                             f'{end_to_sale}'
                             f'🔬Подробнее🔬: {data[0].more_info}',
                             parse_mode='html'
                             )
        await call.answer()


def register_inline_handlers_client(dp: Dispatcher):
    """The function registers handlers"""
    dp.register_callback_query_handler(command_start, Text(startswith=('show_commands')))
    dp.register_callback_query_handler(send_address_shop, Text(startswith=('location')))
    dp.register_callback_query_handler(send_phone_number, Text(startswith=('phone_number')))
    dp.register_callback_query_handler(send_email_address, Text(startswith=('email')))
    dp.register_callback_query_handler(show_catalog, Text(startswith=('catalog')))
    dp.register_callback_query_handler(show_picked_breed, Text(startswith=('breed')))
    dp.register_callback_query_handler(next_call, Text(startswith=('next')))
    dp.register_callback_query_handler(back_call, Text(startswith=('back')))
    dp.register_message_handler(empty)

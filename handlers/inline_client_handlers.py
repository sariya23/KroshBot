from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

from create_bot import bot
from aiogram.dispatcher.filters import Text

from keyboards.inline.inline_breeds import client_keyboard_breeds
from keyboards.inline.inline_commands import client_keyboard_commands

from utils.Parser_class import Parser


class Current:
    pass


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
    breed = call.data.split()[2]
    data = Parser().parse(breed)[int(call.data.split()[1])]

    await bot.edit_message_media(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        media=InputMediaPhoto(media=data.img_url)

    )

    if not data.discount_price:
        await bot.edit_message_caption(
            caption=f'🐇Пушистик породы🐇: <b>{data.breed}</b>\n'
                    f'💵Стоимость счастья💵: {data.old_price}\n'
                    f'🔬Подробнее🔬: {data.more_info}',

            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('next', callback_data=f'next 2 {breed}'))
        )
    else:
        await bot.edit_message_caption(
            caption=f'🐇Пушистик породы🐇: <b>{data.breed}</b>\n'
                    f'💵Стоимость по скидке💵: {data.discount_price}\n'
                    f'<b>⌛СКИДКА ПРОДЛИТСЯ ЕЩЕ⌛</b>: {data.time_to_disc_end}\n'
                    f'🔬Подробнее🔬: {data.more_info}',
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('next1', callback_data=f'next 2 {breed}'))
        )
    await call.answer()


async def show_picked_breed(call: types.CallbackQuery):
    """Send inline keyboard with breeds of rabbits"""
    breed = call.data.split()[1]
    url = Parser.get_url(breed)
    data = Parser().parse(breed)

    if not data[0].discount_price:
        await bot.send_photo(call.from_user.id, data[0].img_url,
                             f'🐇Пушистик породы🐇: <b>{data[0].breed}</b>\n'
                             f'💵Стоимость счастья💵: {data[0].old_price}\n'
                             f'🔬Подробнее🔬: {data[0].more_info}',
                             parse_mode='html',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton('next', callback_data=f'next 1 {breed}'))
                             )
        print(call.data.split())
        await call.answer()

    else:
        await bot.send_photo(call.from_user.id, data[0].img_url,
                             f'🐇Пушистик породы🐇: <b>{data[0].breed}</b>\n'
                             f'💵Стоимость по скидке💵: {data[0].discount_price}\n'
                             f'<b>⌛СКИДКА ПРОДЛИТСЯ ЕЩЕ⌛</b>: {data[0].time_to_disc_end}\n'
                             f'🔬Подробнее🔬: {data[0].more_info}',
                             parse_mode='html',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton('next', callback_data=f'next 1 {breed}'))
                             )
        await call.answer()
    # else:
    #     print(i)
    #     await bot.edit_message_media(
    #         chat_id=call.message.chat.id,
    #         message_id=call.message.message_id,
    #         media=InputMediaPhoto(media=data.img_url)
    #
    #     )
    #     i += 1
    #     await call.answer()

    #
    # for i in data:
    #     if not i.discount_price:
    #         await bot.send_photo(callback.from_user.id, i.img_url,
    #                              f'🐇Пушистик породы🐇: <b>{i.breed}</b>\n'
    #                              f'💵Стоимость счастья💵: {i.old_price}\n'
    #                              f'🔬Подробнее🔬: {i.more_info}',
    #                              parse_mode='html')
    #     else:
    #         await bot.send_photo(callback.from_user.id, i.img_url,
    #                              f'🐇Пушистик породы🐇: <b>{i.breed}</b>\n'
    #                              f'💵Стоимость по скидке💵: {i.discount_price}\n'
    #                              f'<b>⌛СКИДКА ПРОДЛИТСЯ ЕЩЕ⌛</b>: {i.time_to_disc_end}\n'
    #                              f'🔬Подробнее🔬: {i.more_info}',
    #                              parse_mode='html')
    # await callback.answer()
    # await bot.send_message(callback.from_user.id,
    #                        f'Это большинство кроликов породы <b>{english_to_russian[callback.data.split()[1]]}</b>.\n'
    #                        f'Со всеми можешь ознакомиться на нашем сайте: {url}',
    #                        reply_markup=client_keyboard_breeds,
    #                        parse_mode='HTML')


# s = [1, 2, 3, 4, 5]
# p = ['https://tsarskiykrolik.com/wp-content/uploads/2022/11/rubin-600x600.jpg',
#      'https://i.pinimg.com/736x/28/f4/af/28f4afa16adca54153c600a0ea5f63af.jpg']
# i = 0
# # async def test_call(call: types.CallbackQuery):
#     global i
#
#     await bot.edit_message_media(
#         chat_id=call.message.chat.id,
#         message_id=call.message.message_id,
#         media=InputMediaPhoto(media=p[i])
#
#     )
#
#     await bot.edit_message_caption(
#         caption=f'{s[i]}',
#         chat_id=call.message.chat.id,
#         message_id=call.message.message_id,
#         reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('next1', callback_data='next'))
#     )
#     i += 1
#     await call.answer()


def register_inline_handlers_client(dp: Dispatcher):
    """The function registers handlers"""
    dp.register_callback_query_handler(command_start, Text(startswith=('show_commands')))
    dp.register_callback_query_handler(send_address_shop, Text(startswith=('location')))
    dp.register_callback_query_handler(send_phone_number, Text(startswith=('phone_number')))
    dp.register_callback_query_handler(send_email_address, Text(startswith=('email')))
    dp.register_callback_query_handler(show_catalog, Text(startswith=('catalog')))
    dp.register_callback_query_handler(show_picked_breed, Text(startswith=('breed')))
    dp.register_callback_query_handler(next_call, Text(startswith=('next')))
    dp.register_message_handler(empty)

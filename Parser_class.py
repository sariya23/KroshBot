from bs4 import BeautifulSoup
from datetime import timedelta, datetime
from collections import namedtuple

import requests


class Parser:
    """
    Class Parser use for parsing info about rabbits
    General use - take info from div tag with class 'product-wrapper'

    Note:
        Web-site: https://tsarskiykrolik.com/

    Methods:
    --------------------
    get_hours_from_td(data: datetime.timedelta) - Returns hours from timedelta

    convert_hours_to_word(hour: int) - Changes the ending of a word for correct form

    convert_days_to_word(day: int) - Changes the ending of a word for correct form

    parse_date(str_date: str) - Converts str date to datetime type

    format_datetime(date: datetime.timedelta) - Returns a string with the number of days and hours until the end of the discount

    parse(breed: str) - Returns a list of namedtuple with information about rabbits
    """
    def __init__(self):
        pass

    @staticmethod
    def get_hours_from_td(date: timedelta) -> int:
        """Returns hours from timedelta"""
        return date.seconds // 3600

    @staticmethod
    def convert_hours_to_word(hour: int) -> str:
        """Returns correct ending of a word(час/часа/часов)"""
        if hour <= 4:
            return 'часа'
        else:
            return 'часов'

    @staticmethod
    def convert_days_to_word(day: int) -> str:
        """Returns correct ending of a word(день, дня, дней)"""
        if day == 1:
            return 'день'
        elif 2 <= day <= 4:
            return 'дня'
        else:
            return 'дней'

    @staticmethod
    def parse_date(str_date: str) -> datetime:
        """Returns date at datetime type"""
        return datetime.strptime(str_date, '%Y-%m-%d  %H:%M:%S')

    def format_datetime(self, date: timedelta) -> str:
        """Returns a string with the number of days and hours until the end of the discount.
        If days until the end of discount less 0, only the hours are returned"""
        time_end = (date.days, self.get_hours_from_td(date))

        if time_end[0] == 0 and time_end[1] > 0:  # if days < 0
            return f'{time_end[1]} {self.convert_hours_to_word(time_end[1])}'
        else:
            return f'{time_end[0]} {self.convert_days_to_word(time_end[0])} и {time_end[1]} {self.convert_hours_to_word(time_end[1])}'

    def parse(self, breed: str) -> list[namedtuple]:
        """Takes breed from user(inline-button) and parse info about it from site.
        The Exception is raised if no discount in block"""

        breeds = {
            'belichij': 'belichij',
            'germelin': 'germelin',
            'karlikovyj-baran': 'karlikovyj-baran',
            'minor': 'minor',
            'minilop': 'minilop',
            'niderlandskij': 'niderlandskij',
            'xotot': 'xotot',
            'cvetnoj-karlik': 'cvetnoj-karlik'
        }

        URL = f'https://tsarskiykrolik.com/product-category/kroliki/?filter_poroda={breeds[breed]}'
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, 'html.parser')
        products = soup.find_all('div', class_='product-wrapper')
        res = []

        for block in products:
            breed = block.find('h3').text.strip()
            price = block.find('span', class_='price').text.split()
            img_url = block.find('img').get('data-srcset').split(', ')[0][:-4]
            more_info = block.find('h3').find('a')['href']
            end_discount = timedelta(days=0, hours=0)
            time_to_end = timedelta(days=0, hours=0)

            try:
                end_discount = (
                    self.parse_date(
                        block.find(
                            'div',
                            class_='wd-product-countdown wd-timer woodmart-product-countdown woodmart-timer').attrs[
                            'data-end-date'])
                )

                current_date = datetime.now()
                time_to_end = end_discount - current_date + timedelta(hours=3)

            except AttributeError:
                pass

            old_price = ''.join(price[:price.index('₽') + 1])
            discount_price = ''.join(price[price.index('₽') + 1:])
            Rabbit = namedtuple('Rabit', 'breed, img_url, old_price, discount_price, time_to_disc_end, more_info')
            rabbit = Rabbit(breed, img_url, old_price, discount_price, self.format_datetime(time_to_end), more_info)

            res.append(rabbit)

        return res


if __name__ == '__main__':
    a = Parser()
    print(*a.parse('germelin'), sep='\n')
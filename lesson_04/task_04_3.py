# Доработать функцию currency_rates: теперь она должна возвращать курс валюты и дату, которая передаётся в ответе
# сервера. Название новой функции currency_rates_advanced.
#
# Формат вывода результата:
#     Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
#
# Техническое задание
#     1. Все требования задания 2 остаются в силе.
#     2. Функция должна вернуть список или кортеж, содержащий дату и курс валюты.
#     3. Дата должна быть объектом date пакета datetime стандартной библиотеки. Для ее создания используйте функции
#     пакета datetime. Если это слишком сложно - оставьте дату строкой.
#
# Алгоритм
#     1. Посмотрите ответ сервера, как с минимальными усилиями вытащить оттуда дату?
#     2. Подумайте можно ли, и правильно ли вызывать из этой функции функцию предыдущей задачи: currency_rates
#     3. Если есть требования, что мы используем обе функции в своей работе, как соблюсти принцип DRY?


from requests import get
import datetime


def tag_slice(string, tag):
    """Find and return substring between XML tags.
    Required keyword arguments:
    string: a string to search for.
    tag: a tag to search for.
    """
    tags = [f'<{tag}', f'</{tag}>']
    keys = list()
    for each in tags:
        found_key = string.find(each)
        keys.append(found_key)
    start, end = keys
    output = string[start+len(tags[0])+1:end]
    return output


def currency_rates(url, currency):
    """Return the currency rate.
    Required keyword arguments:
    url: site address with currency rates.
    currency: three-letter currency code.
    """
    full_text = get(url).text.split('</Valute><Valute ID="')
    output = dict()
    for each in full_text:
        valute = tag_slice(each, 'CharCode')
        value = tag_slice(each, 'Value').replace(',', '.')
        output[valute] = float(value)
    return output.get(currency.upper())


def currency_rates_advanced(url, currency):
    """Return the tuple with the date and currency rate.
    Required keyword arguments:
    url - site address with currency rates.
    currency: three-letter currency code.
    """
    date_string = get(url).headers.get('Date')
    long_date = datetime.datetime.strptime(date_string, '%a, %d %b %Y %X %Z')
    short_date = datetime.datetime.strftime(long_date, '%Y, %m, %d')
    splitted_date = short_date.split(',')
    for key, val in enumerate(splitted_date):
        splitted_date[key] = int(val)
    year, month, day = tuple(splitted_date)
    output = [datetime.date(year, month, day)], currency_rates(url, currency)
    return output


url = 'http://www.cbr.ru/scripts/XML_daily.asp'
print(currency_rates_advanced(url, 'USd'))
print(currency_rates_advanced(url, 'EuR'))
print(currency_rates_advanced(url, 'GBP'))
print(currency_rates_advanced(url, 'GBP2'))

# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, …) и возвращающую курс этой валюты по отношению к рублю.
#
# Формат вывода результата:
#     Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
#
# Техническое задание
#     1. Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
#     Выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. В каком формате возвращен
#     ответ?
#     2. Функция принимает два аргумента: строка с URL, куда стучимся и строку с кодом валюты (только одной).
#     Возвращает результат числового типа, например float. Если в качестве аргумента передали код валюты, которого нет
#     в ответе, вернуть объект None.
#     3. Для извлечения данных использовать только методы объект str.
#     4. Сделать работу функции не зависящей от того, в каком регистре был передан аргумент.
#     5. Функция должна корректно обрабатывать любой код валюты. Правильность параметра url можно не проверять.
#     6. Вводить коды валют с клавиатуры (input) необязательно.
#
# Алгоритм
#     1. Пример использования requests есть в методичке.
#     2. Внимательно посмотрите все методы объекта str, которыми вы можете пользоваться. Обратите внимание, что
#     у методов могу быть параметры, которые сильно облегчат вам работу.
#     3. Помните, срез строки создает копию. Уверены ли вы, что вам нужна копия именно такого размера? Это увеличивает
#     время выполнения и расходует память. Аналогично функция поиска требует времени для работы, можно ли оптимизировать
#     поиск?
#     4. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли
#     усложняется код функции при этом?
#     5. Вспомните в каких случаях функция возвращает None.

import requests


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
    response = requests.get(url)
    full_text = response.text.split('</Valute><Valute ID="')
    output = dict()
    for each in full_text:
        valute = tag_slice(each, 'CharCode')
        value = tag_slice(each, 'Value').replace(',', '.')
        output[valute] = float(value)
    return output.get(currency.upper())


url = 'http://www.cbr.ru/scripts/XML_daily.asp'

print(currency_rates(url, 'USd'))
print(currency_rates(url, "EuR"))
print(currency_rates(url, "GBP"))
print(currency_rates(url, "GBP2"))

print('\nПроверка типа возвращаемого ответа:')
a = currency_rates(url, 'USd')
print(type(a))

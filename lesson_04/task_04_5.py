from utils import currency_rates

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_input = input('Введите буквенный код валюты: ')
output = currency_rates(url, currency_input)

if output is None:
    output = 'Не найдена валюта'

print(currency_input.upper(), ': ', output, sep='')

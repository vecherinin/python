from utils import currency_rates

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_input = input('Введите трёхбуквенный код валюты: ')
output = currency_rates(url, currency_input)

if len(currency_input) == 0:
    print('Код валюты не введён.')
elif len(currency_input) > 3 or len(currency_input) < 3:
    print('Ошибка ввода.\nКод валюты должен состоять из трёх букв.')
elif output is None:
    output = 'Не найдена валюта'
    print(currency_input.upper(), ': ', output, sep='')
else:
    print(currency_input.upper(), ': ', output, sep='')

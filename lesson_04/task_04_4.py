from utils import currency_rates, currency_rates_advanced

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

print(currency_rates(url, 'USd'))
print(currency_rates(url, 'EuR'))
print(currency_rates(url, 'GBP'))
print(currency_rates(url, 'GBP2'))
print('\n')
print(currency_rates_advanced(url, 'USd'))
print(currency_rates_advanced(url, 'EuR'))
print(currency_rates_advanced(url, 'GBP'))
print(currency_rates_advanced(url, 'GBP2'))

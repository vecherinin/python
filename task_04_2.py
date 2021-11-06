import requests


def tag_slice(string, tag):
    """Find and return substring between XML tags
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
    response = requests.get(url)
    full_text = response.text.split('</Valute><Valute ID="')
    output = dict()
    for each in full_text:
        valute = tag_slice(each, 'CharCode')
        value = tag_slice(each, 'Value')
        output[valute] = float(value.replace(',', '.'))
    return output.get(currency.upper())


url = 'http://www.cbr.ru/scripts/XML_daily.asp'

print(currency_rates(url, 'USd'))
print(currency_rates(url, "EuR"))
print(currency_rates(url, "GBP"))
print(currency_rates(url, "GBP2"))

print('\nПроверка типа возвращаемого ответа:')
a = currency_rates(url, 'USd')
print(type(a))
import datetime
from requests import get


def tag_slice(string, tag):
    """Find and return substring between XML tags."""
    tags = [f'<{tag}', f'</{tag}>']
    keys = list()
    for each in tags:
        found_key = string.find(each)
        keys.append(found_key)
    start, end = keys
    output = string[start+len(tags[0])+1:end]
    return output


def currency_rates(url, currency):
    """Return the currency rate."""
    full_text = get(url).text.split('</Valute><Valute ID="')
    output = dict()
    for each in full_text:
        valute = tag_slice(each, 'CharCode')
        value = tag_slice(each, 'Value').replace(',', '.')
        output[valute] = float(value)
    return output.get(currency.upper())


def currency_rates_advanced(url, currency):
    """Return the tuple with the date and currency rate."""
    date_string = get(url).headers.get('Date')
    long_date = datetime.datetime.strptime(date_string, '%a, %d %b %Y %X %Z')
    short_date = datetime.datetime.strftime(long_date, '%Y, %m, %d')
    splitted_date = short_date.split(',')
    for key, val in enumerate(splitted_date):
        splitted_date[key] = int(val)
    year, month, day = tuple(splitted_date)
    output = [datetime.date(year, month, day)], currency_rates(url, currency)
    return output

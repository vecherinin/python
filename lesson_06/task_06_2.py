# [Задача со звездочкой]: усложненный вариант задания 1. Найти IP адрес спамера
# и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Спамер — это клиент, отправивший больше всех запросов.
#
# Формат вывода результата:
#     1. Вывести IP спамера и количество запросов от него.
#
# Техническое задание
#     1. Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
#     2. У нас изначально нет никакой информации о максимальном количестве запросов. Его надо определить из лог-файла.
#
# Примечание:
#     1. Не используйте затратные операций типа сортировки и поисков. Они здесь абсолютно избыточны.
#     Для примера представьте, что более половина лог-файла - это запросы от спамера.
#     Оцените эффективность вашего алгоритма в таком случае.
#     2. Уверены ли вы, что максимальное кол-во запросов - уникально? Т.е. найденный спамер - только один?
#     Или таких спамеров может быть несколько?

import requests

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
txt = response.text.split(')"')


def find_addr(input, limiter_start, limiter_end):
    output = list()
    lines = input[limiter_start:limiter_end]
    for each in lines:
        remote_addr_idx = each.find(' - - ')
        remote_addr = each[:remote_addr_idx].strip('\n')
        output.append(remote_addr)
    return output


def count_dict(input):
    output = dict()
    for each in input:
        number = input.count(each)
        output[each] = number
    return output


def find_spammer(input):
    spam_requests = max(input.values())
    spammer = list(input.keys())[list(input.values()).index(spam_requests)]
    return f'Spammer`s IP: {spammer}\nNumber of requests: {spam_requests}'


# Ограничитель поиска
limiter_start = 0
limiter_end = 10000

array = find_addr(txt, limiter_start, limiter_end)
output = count_dict(array)
print(find_spammer(output))

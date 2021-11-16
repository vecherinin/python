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
from collections import Counter

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
txt = response.text.split(')"')


def find_addr(input):
    """Получить список IP-адресов"""
    ip_list = list()
    for each in input:
        end_index = each.find(' - - ')
        remote_addr = each[:end_index].strip('\n')
        ip_list.append(remote_addr)
    return ip_list


ip_dict = Counter(find_addr(txt))
spam_requests = max(ip_dict.values())
spammer = list(ip_dict.keys())[list(ip_dict.values()).index(spam_requests)]
print(f'Spammer`s IP: {spammer}\nNumber of Requests: {spam_requests}')

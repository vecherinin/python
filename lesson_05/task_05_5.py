# Задан список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
#
# Техническое задание
#     1. Здесь нет условия создавать итератор/генератор или comprehensions.
#     2. Сохранение исходного порядка в результирующем списке обязательно.
#
# Примеры/Тесты:
#     src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#     result = [23, 1, 3, 10, 4, 11]
#
# Алгоритм
#     1. Сначала найдите способ определить уникальность элемента в списке.
#     Затем подумайте о сохранении порядка исходного списка.
#     2. Оцените эффективность вашего алгоритма.
#     Вспомните о множестве - объекте, который пройден на этом уроке, его преимуществах. Как его можно применить.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = set()

for el in src:
    if el not in result:
        result.add(el)
    else:
        result.discard(el)

print(sorted(result, key=src.index))

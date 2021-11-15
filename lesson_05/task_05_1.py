# Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield,
# полностью истощить генератор.
#
# Формат вывода результата:
#     Программа явно должна закончиться на StopIteration
#
# Техническое задание
#     1. n - любое положительное число.
#     2. Не путайте истощение итератора и печать его значений. Явно дойдите до StopIteration. Истощение генератора -
#     любым удобным для вас способом. Например создаем генератор в программе, а истощаем руками в консоли.
#     3. Создание генератора сделайте внутри функции iterator_without_yield(n), примающей аргументом n любое
#     положительное число и возвращающей генератор.


def iterator_without_yield(n):
    if n > 0:
        gen = (el for el in range(1, n+1, 2))
        return gen


# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200. Все остальное как в основном задании.


def iterator_without_yield_advanced(n):
    if n > 0:
        gen = (el for el in range(1, n+1, 2) if el**2 < 200)
        return gen


# Для тестирования (аргумент_1 - любое положительное число):
gen1 = iterator_without_yield(11)
gen2 = iterator_without_yield_advanced(1000)

# Ниже можно раскомментить для истощения первого итератора:
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

# для истощения второго итератора:
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))

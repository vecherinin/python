# Реализовать склонение слова «процент» для чисел до 234.
# Например:
# Задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.
#
# Формат вывода результата:
#   0 процентов
#   1 процент
#   2 процента
#   3 процента
#   4 процента
#   5 процентов
#   и т.п.
#
# Алгоритм:
#   Ваш алгоритм должен корректно работать и для интервала от 1 до 234,
#   но для любого числа(заведенного в код), например от 1 до 1000.
#   Правила склонения здесь достаточно просты: всего три варианта.


start_number = 0
finish_number = 234
percent = ' процент'
ending_a = 'а'
ending_ov = 'ов'

while start_number >= 0:
    remain = start_number % 100
    last_n = remain % 10
    output = str(start_number) + percent
    if remain >= 11 and remain <= 19:
        print(output + ending_ov)
    elif last_n == 1:
        print(output)
    elif last_n >= 2 and last_n <= 4:
        print(output + ending_a)
    else:
        print(output + ending_ov)
    start_number = start_number + 1
    if start_number > finish_number:
        break


# Задаем диапазон нечётных чисел для возведения в куб
start_num = 1
finish_num = 1000

numbers_sum = 0
while start_num <= finish_num:
    # Отбрасываем чётные числа
    if start_num % 2 != 0:
        # Возводим число в куб
        cube = start_num**3
        # Для суммы разрядов числа
        total = 0
        # Для целочисленного деления
        x = 1
        while cube // x > 0:
            # Получение разрядов чисел
            n = (cube // x) % 10
            # Изменение целочисленного делителя
            x = x * 10
            # Сумма разрядов чисел
            total += n
        # Выборка делимых на 7 сумм разрядов чисел
        if total % 7 == 0:
            # Суммирование основания
            numbers_sum += start_num
            print(start_num, '^3:', cube, 'sum:', numbers_sum, '[', total, ']')
        # Для перехода к следующему нечётному числу
        start_num += 2

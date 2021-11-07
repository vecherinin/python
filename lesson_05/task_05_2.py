# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200. Все остальное как в основном задании.


def iterator_without_yield_advanced(n):
    if n > 0:
        gen = (el for el in range(1, n+1, 2) if el**2 < 200)
        return gen

n = 1000  # Любое положительное число
gen2 = iterator_without_yield_advanced(n)

# Можно раскомментить ниже для истощения итератора:
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
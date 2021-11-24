# Написать декоратор для логирования типов позиционных аргументов функции:
#
# Техническое задание:
#     Если аргументов несколько - выводить данные о каждом через запятую.
#     Все выводы должны быть в функции обертке(декораторе)
#     После того как вы «обернули» функцию, «задекорировали» убедитесь,
#     что аргументы и возвращаемое значение остались как у исходной функции.


def type_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Call for: {func.__name__}")
        value = func(*args)
        print(f"{args[0]}: {type(value)}")
        if kwargs:
            output = list()
            for item in kwargs:
                output.append(f"'{item}' = {kwargs[item]}: {type(kwargs[item])}")
            print(', '.join(output))
            # return value
        print(f"Result: {value}, type: {type(value)}")
    return wrapper


@type_logger
def render_input(*args):
   return 1

@type_logger
def calc_cube(x):
   return x ** 3


# Для проверки выполнения скрипта:
# print('\n')
# calc_cube(5)
# print('\n')
# render_input(1, a = 2, b = True, c = "q")

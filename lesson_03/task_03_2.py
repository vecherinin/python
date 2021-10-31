# [Задача со звездочкой]: усложненный вариант задания 1.
# Написать функцию num_translate_adv, которая корректно обработает числительные,
# начинающиеся с заглавной буквы. Если перевод сделать невозможно, вернуть объект None.
#
# Примеры/Тесты:
#     >>> num\_translate\_adv("One")
#     "Один"
#     >>> num\_translate\_adv("two")
#     "два"
#
# Техническое задание
#     Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
#     Считаем, что только первая буква может быть заглавной.
#     Обратите внимание, что функция возвращает перевод в том же регистре как и приняла.


def num_translate_adv(num):
    if num.istitle():
        in_russian = eng_to_rus.get(num.lower())
        if in_russian is not None:
            return in_russian.capitalize()
        else:
            return None
    elif num.islower():
        in_russian = eng_to_rus.get(num)
        return in_russian
    else:
        return None


eng_to_rus = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
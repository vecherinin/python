# Написать функцию num_translate, переводящую числительные от 0 до 10 c английского
# на русский язык. Если перевод сделать невозможно, вернуть объект None.
#
# Примеры/Тесты:
#     >>> num\_translate("one")
#     "один"
#     >>> num\_translate("eight")
#     "восемь"
#
# Техническое задание
#     Функция num_translate возвращает строку перевод. Или возвращает None, если перевести невозможно.
#     Здесь нет требований на регистр входного слова. Возвращается результат в нижнем регистре.


def num_translate(num):
    if num.isalpha():
        if num.istitle():
            return eng_to_rus.get(num.lower())
        else:
            return eng_to_rus.get(num)
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
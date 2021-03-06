# [Задача со звездочкой]: усложненный вариант задания 3.
# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи —
# первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания
# и содержащие записи, в которых фамилия начинается с соответствующей буквы.
#
# Техническое задание
#     Количество передаваемых строк в функцию может быть любым. Считаем, что переданы будут только корректные строки.
#     Вернуть словарь, с ключами, отсортированными в алфавитном порядке.
#
# Примеры/Тесты:
#     >>> thesaurus\_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев",
#     "Илья Иванов", "Анна Савельева", "Василий Суриков")
#     {
#        'А': {'П': ['Петр Алексеев']},
#        'И': {'И': ['Илья Иванов']},
#        'С': {
#               'А': ['Алла Сидорова', 'Анна Савельева'],
#               'В': ['Василий Суриков'],
#               'И': ['Иван Сергеев', 'Инна Серова']
#             }
#     }


def thesaurus_adv(*list_of_names):
    output = {}
    names = sorted(list_of_names)
    for full in names:
        name = str(full).split()
        first = str(name[0])
        last = str(name[1])
        lt_first = first[0]
        lt_last = last[0]
        if lt_last not in output:
            output[lt_last] = {}
        if lt_first not in output[lt_last]:
            output[lt_last][lt_first] = []
            output[lt_last][lt_first].append(full)
    sorted_output = {}
    for i in sorted(output.keys()):
        sorted_output[i] = output[i]
    return sorted_output

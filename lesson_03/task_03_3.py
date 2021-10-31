# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имен,
# а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#
# Техническое задание
#     Количество передаваемых имен в функцию может быть любым.
#     Считаем, что переданы будут только корректные строки.
#     Вернуть словарь с ключами, отсортированными в алфавитном порядке.
#
# Примеры/Тесты:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
#
# Алгоритм
#     Вспомните как обработать произвольное количество передаваемых параметров.


def thesaurus(* names):
    output = {}
    for name in sorted(names):
        fst_letter = name[0]
        if fst_letter not in output:
            output[fst_letter] = []
        output[fst_letter].append(name)
        sorted(output)
    return output

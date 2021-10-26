arr = [
    ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'],
    ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
]

for list in arr:
    print('\nИсходный список:\n', list)
    i = 0
    while i < len(list):
        if list[i].isdigit():
            list[i] = list[i].zfill(2)
            list.insert(i, '"')
            list.insert(i + 2, '"')
            i += 2
        elif list[i][0] in "+-":
            list[i] = list[i].zfill(3)
            list.insert(i, '"')
            list.insert(i + 2, '"')
            i += 2
        else:
            i += 1
    print('\nРезультирующий список:\n', list)

    string = ' '.join(list).split('"')

    idx = 1
    while idx < len(string):
        string[idx] = string[idx].strip()
        idx += 2
    print('\nСтрока:\n', '"'.join(string),'\n\n')

original_lists = [
    ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'],
    ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
]
# Вставка в список отдельных строк с кавычками, до числа и после
def add_quotes(x):
    x.insert(i, '"')
    x.insert(i + 2, '"')

for each_list in original_lists:
    print('\nИсходный список:\n', each_list)
    i = 0
    while i < len(each_list):
        # Добавление кавычек для числительных без знаков + или -
        if each_list[i].isdigit():
            # Добавление нуля перед числом из одного знака
            each_list[i] = each_list[i].zfill(2)
            add_quotes(each_list)
        elif each_list[i][0] in "+-":
            each_list[i] = each_list[i].zfill(3)
            add_quotes(each_list)
        else:
            i += -1
        i += 2
    print('\nРезультирующий список:\n', each_list)

    # Удаление пробелов между кавычками и числом (со знаком или без)
    each_list = ' '.join(each_list).split('"')
    idx = 1
    while idx < len(each_list):
        each_list[idx] = each_list[idx].strip()
        idx += 2
    print('\nСтрока:\n', '"'.join(each_list),'\n\n')

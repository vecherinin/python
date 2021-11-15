# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл.
# Проверить сохранённые данные.
#
# Техническое задание
#     1. Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО
#     соответствует 1-ая строка файла с хобби и т.п.
#     2. При хранении данных используется принцип: одна строка — один пользователь.
#     3. Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов.
#     4. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
#     то для оставшихся ФИО использовать вместо хобби None.
#     5. Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
#     6. При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
#     7. Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.

file_fio = open('task_3_users.csv', 'r', encoding='utf-8')
file_hobbies = open('task_3_hobby.csv', 'r', encoding='utf-8')

fio = file_fio.read()
list_fio = fio.replace(',', ' ').split('\n')
hobbies = file_hobbies.read()
list_hobbies = hobbies.split('\n')

output = dict()
i = 0
while True:
    if i >= len(list_hobbies):
        if i < len(list_fio):
            output[list_fio[i]] = None
        else:
            break
    elif i > len(list_fio):
        break
        exit(1)
    elif i < len(list_fio) and i < len(list_hobbies):
        output[list_fio[i]] = list_hobbies[i]
    i += 1

result = open('task_3_rezult.txt', 'w+', encoding='utf-8')
result.write(str(output))

file_fio.close()
file_hobbies.close()
result.close()

file_fio = open('task_3_users.csv', 'r', encoding='utf-8')
file_hobbies = open('task_3_hobby.csv', 'r', encoding='utf-8')
fio = file_fio.read()
hobbies = file_hobbies.read()
list_fio = fio.replace(',', ' ').split('\n')
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

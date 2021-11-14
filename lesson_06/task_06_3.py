file_fio = open('task_3_users.csv', 'r', encoding='utf-8')
file_hobbies = open('task_3_hobby.csv', 'r', encoding='utf-8')
fio = file_fio.read()
hobbies = file_hobbies.read()
list_fio = fio.replace(',', ' ').split('\n')
list_hobbies = hobbies.split('\n')

i = 0
if len(list_fio) > len(list_hobbies):
    while True:
        dict = {list_fio[i]:list_hobbies[i]}
# i = 0
# while True:
#     if i > len(list_hobbies):
#         output = {list_fio[i]: None}
#     elif i > len(list_fio):
#         exit(1)
#     else:
#         output = {list_fio[i]: list_hobbies[i]}
#
#     i += 1

print(dict)
# print(len(list_fio))
file_fio.close()
file_hobbies.close()
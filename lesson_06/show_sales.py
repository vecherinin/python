from sys import argv

file_db = open('bakery.csv', 'r', encoding='utf-8')
lines = file_db.readlines()


def print_output(list):
    for each in list:
        print(each.strip('\n'))


if len(argv) == 1:
    print_output(lines)
elif ''.join(argv[1:]).isdigit() is False:
    print("Ошибка типа передаваемых параметров.")
elif len(argv) == 2:
    if int(argv[1])-1 >= len(lines):
        print("Данные с заданными параметрами отсутствуют.")
    else:
        list_lines = lines[int(argv[1])-1:]
        print_output(list_lines)
elif len(argv) == 3:
    list_lines = lines[int(argv[1])-1:int(argv[2])]
    print_output(list_lines)
else:
    print('Ошибка ввода. Максимально допустимое количество чисел - 2.')

file_db.close()

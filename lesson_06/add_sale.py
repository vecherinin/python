from sys import argv

file_db = open('bakery.csv', 'a+', encoding='utf-8')
if len(argv) == 1:
    print('Ошибка ввода. Сумма продажи не введена.')
elif len(argv) == 2:
    if str(argv).isdigit:
        file_db.write(str(argv[1]) + '\n')
    else:
        print('Ошибка ввода. Сумма продажи должна быть числом.')

file_db.close()
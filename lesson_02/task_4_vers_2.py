# Второй вариант решения задачи с красивым выводом цен, отсортированные по возрастанию
price_list = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 534, 999.99, 254.80, 75.05, 116.6, 402.75]
print('Исходный список:', price_list, sep='\n')

def float_to_string(x):
    for i in range(len(x)):
        rub_in_kop = int(x[i] * 100) # Рубли в копейках
        rub = rub_in_kop // 100 # Целых рублей
        kop = rub_in_kop % 100
        x[i] = f"{rub} руб {kop:02d} коп"
def string_to_float(x):
    for i in range(len(x)):
        x[i] = x[i].replace(' руб ', '').replace(' коп', '')
        x[i] = float(x[i]) / 100

float_to_string(price_list)
print('\nСтрока:', ', '.join(price_list), sep='\n')

string_to_float(price_list)
print('\nДоказательство операции in place:', '\nid перед сортировкой', id(price_list))

price_list.sort()
float_to_string(price_list)
print('\nЦены, отсортированные по возрастанию:', ', '.join(price_list), sep='\n')
print('\nid после сортировки', id(price_list))

string_to_float(price_list)
sorted_price = sorted(price_list, reverse=True)
print('\n5 самых дорогих товаров:')
for i in range(5):
    print('{0:g}'.format(sorted_price[i]))

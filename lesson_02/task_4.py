price_list = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 534, 999.99, 254.80, 75.05, 116.6, 402.75]
print('Исходный список:', price_list, sep='\n')

for i in range(len(price_list)):
    rub_in_kop = int(price_list[i] * 100)
    rub = rub_in_kop // 100
    kop = rub_in_kop % 100
    price_list[i] = f"{rub} руб {kop:02d} коп"
print('\nСтрока:', ', '.join(price_list), sep='\n')

for i in range(len(price_list)):
    price_list[i] = price_list[i].replace(' руб ', '').replace(' коп', '')
    price_list[i] = float(price_list[i]) / 100

print('\nДоказательство операции in place:', '\nid перед сортировкой', id(price_list))
price_list.sort()
print('\nЦены, отсортированные по возрастанию:', price_list, sep='\n')
print('\nid после сортировки', id(price_list))

sorted_price = sorted(price_list, reverse=True)
print('\n5 самых дорогих товаров:')
for i in range(5):
    print('{0:g}'.format(sorted_price[i]))

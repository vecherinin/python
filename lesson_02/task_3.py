input = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

i = 0
while i < len(input):
    input[i] = input[i].split(' ')
    input[i] = input[i][-1].capitalize()
    print(f'Привет, {input[i]}!')
    i += 1

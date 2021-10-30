duration = int(input('Введите продолжительность времени в секундах: \n'))

whole_minute = 60
whole_hour = whole_minute * 60
all_day = whole_hour * 24
remainder = duration % all_day

hours = remainder // whole_hour
minutes = remainder % whole_hour // whole_minute
seconds = remainder % whole_hour % whole_minute

if duration < whole_minute:
    print('До минуты:', str(seconds), 'сек.')
elif duration < whole_hour:
    print('До часа:', str(minutes), 'мин', str(seconds), 'сек.')
elif duration < all_day:
    print('До суток:', str(hours), 'час', str(minutes), 'мин', str(seconds), 'сек.')
else:
    print(str(duration // all_day), 'дн', str(hours), 'час', str(minutes), 'мин', str(seconds), 'сек.')
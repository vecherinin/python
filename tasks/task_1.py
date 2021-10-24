duration = int(input('Введите продолжительность времени в секундах: '))

minute = 60
hour = minute*60
day = hour*24

h = duration % day // hour
m = duration % day % hour // minute
s = duration % day % hour % minute

if duration < minute:
    print('До минуты: ' + str(s) + ' сек.')
elif duration < hour:
    print('До часа: ' + str(m) + ' мин ' + str(s) + ' сек.')
elif duration < day:
    print('До суток: ' + str(h) + ' час ' + str(m) + ' мин ' + str(s) + ' сек.')
else:
    print(str(duration // day) + ' дн ' + str(h) + ' час ' + str(m) + ' мин ' + str(s) + ' сек.')
start_number = 0
finish_number = 234
percent = ' процент'
ending_a = 'а'
ending_ov = 'ов'

while start_number >= 0:
    remain = start_number % 100
    last_n = remain % 10
    output = str(start_number) + percent
    if remain >= 11 and remain <= 19:
        print(output + ending_ov)
    elif last_n == 1:
        print(output)
    elif last_n >= 2 and last_n <= 4:
        print(output + ending_a)
    else:
        print(output + ending_ov)
    start_number = start_number + 1
    if start_number > finish_number:
        break


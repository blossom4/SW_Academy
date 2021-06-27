# SWEA 2056

T = int(input())
for tc in range(1, T + 1):
    date = list(map(int, input()))
    year = []
    month = []
    day = []
    flag = 0
    if date[4] > 1:
        print('#{} {}'.format(tc, -1))
        flag = 1
    elif date[5] > 2:
        print('#{} {}'.format(tc, -1))
        flag = 1
    elif date[4] == 0 and date[5] == 0:
        print('#{} {}'.format(tc, -1))
        flag = 1
    elif date[6] == 0 and date[7] == 0:
        print('#{} {}'.format(tc, -1))
        flag = 1
    elif date[4] == 0 and (date[5] == 1 or date[5] == 3 or date[5] == 5 or date [5] == 7 or date [5] == 8):
        if date[6] == 3 and date[7] > 1:
            print('#{} {}'.format(tc, -1))
            flag = 1
    elif date[4] == 0 and (date[5] == 4 or date[6] == 6 or date[5] == 9):
        if date[6] == 3 and date[7] > 0:
            print('#{} {}'.format(tc, -1))
            flag = 1
    elif date[4] == 0 and date[5] == 2:
        if date[6] > 2:
            print('#{} {}'.format(tc, -1))
            flag = 1
        elif date[6] == 2 and date[7] > 8:
            print('#{} {}'.format(tc, -1))
            flag = 1
    elif date[4] == 1 and (date[5] == 0 or date[5] == 2):
         if date[6] == 3 and date[7] > 1:
                print('#{} {}'.format(tc, -1))
                flag = 1
    elif date[4] == 1 and date[5] == 1:
         if date[6] == 3 and date[7] > 0:
                print('#{} {}'.format(tc, -1))
                flag = 1
    if flag == 0:
        for i in range(len(date)):
            if i < 4:
                year.append(str(date[i]))
            elif i < 6:
                month.append(str(date[i]))
            else:
                day.append(str(date[i]))
        res_year = str.join('', year)
        res_month = str.join('', month)
        res_day = str.join('', day)
        res_date = (res_year + '/' + res_month + '/' + res_day)
        print('#{} {}'.format(tc, res_date))
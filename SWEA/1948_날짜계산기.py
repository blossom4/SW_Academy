# SWEA 1948

def get_days(m1, d1, m2, d2):
    day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    day_sum = 0
    days = d2 - d1 + 1
    for i in range(m1, m2):
        day_sum += day_list[i]
    day_sum += days
    return day_sum

T = int(input())
for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    res = get_days(m1, d1, m2, d2)
    print('#{} {}'.format(tc, res))
    
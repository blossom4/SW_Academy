# SWEA 1970

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt_list = [0 for _ in range(8)]
    for i in range(8):
        if N // money_list[i] > 0:
            cnt_list[i] += N // money_list[i]
            N = N - money_list[i] * (N // money_list[i])
    for i in range(8):
        cnt_list[i] = str(cnt_list[i])
    res = str.join(' ', cnt_list)
    print('#{}\n{}'.format(tc, res))
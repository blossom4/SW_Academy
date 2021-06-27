# SWEA 1204

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    d = dict()
    max_value = -1
    max_num = 0
    for num in num_list:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
        if max_value < d.get(num):
            max_value = d.get(num)
    for num in num_list:
        if d.get(num) == max_value and num > max_num:
            max_num = num

    print('#{} {}'.format(tc, max_num))
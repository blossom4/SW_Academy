# SWEA 2071

def get_avg(arr):
    total_sum = 0
    for i in range(10):
        total_sum += arr[i]
    res = round(total_sum / 10)
    return res

T = int(input())
for tc in range(1, T + 1):
    N_list = list(map(int, input().split()))
    print('#{} {}'.format(tc, get_avg(N_list)))
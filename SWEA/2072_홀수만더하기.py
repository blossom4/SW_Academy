# SWEA 2072

def odd_sum(arr):
    total_sum = 0
    for i in range(10):
        if arr[i] % 2:
            total_sum += arr[i]
    return total_sum

T = int(input())
for tc in range(1, T + 1):
    n_list = list(map(int, input().split()))
    res = odd_sum(n_list)
    print('#{} {}'.format(tc, res))
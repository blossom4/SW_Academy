# SWEA 1959

def get_multiple_sum(arr1, arr2):
    max_value = -1000000000
    # 긴 배열 선택
    if len(arr1) < len(arr2):
        N = arr1
        M = arr2
    else:
        N = arr2
        M = arr1
    for i in range(len(M) - len(N) + 1):
        total_sum = 0
        for j in range(len(N)):
            total_sum += N[j] * M[i + j]
        if max_value < total_sum:
            max_value = total_sum
    return max_value

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    res = get_multiple_sum(N_list, M_list)
    print('#{} {}'.format(tc, res))
# SWEA 2068

def find_max(arr):
    max_value = -1
    for i in range(len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value

T = int(input())
for tc in range(1, T + 1):
    n_list = list(map(int, input().split()))
    print('#{} {}'.format(tc, find_max(n_list)))
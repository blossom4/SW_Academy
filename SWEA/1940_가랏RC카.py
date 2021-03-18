# SWEA 1940

def get_distance(arr):
    present_D = 0
    present_V = 0
    for i in range(len(arr)):
        if arr[i][0] == 1:
            present_V += arr[i][1]
            present_D += present_V
        elif arr[i][0] == 2:
            if present_V - arr[i][1] >= 0:
                present_V -= arr[i][1]
                present_D += present_V
        else:
            present_D += present_V
    return present_D

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr =[]
    for i in range(N):
        N_list = list(map(int, input().split()))
        arr.append(N_list)
    for i in range(N):
        if arr[i] == [0]:
            arr[i] = [0, 0]
    res = get_distance(arr)
    print('#{} {}'.format(tc, res))

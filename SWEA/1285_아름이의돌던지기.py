# SWEA 1285

def shortest(arr):
    min_distance = 100001
    cnt = 0
    res = ''
    for i in range(len(arr)):
        if abs(arr[i]) < min_distance:
            min_distance = abs(arr[i])
    for i in range(len(arr)):
        if abs(arr[i]) == min_distance:
            cnt += 1
    res += str(min_distance)
    res += ' '
    res += str(cnt)
    return res

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))
    res = shortest(N_list)
    print('#{} {}'.format(tc, res))
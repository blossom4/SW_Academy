# SWEA 1961

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[N - j - 1][i], end = '')
        print(' ', end='')
        for j in range(N):
            print(arr[N - i - 1][N - j - 1], end = '')
        print(' ', end='')
        for j in range(N):
            print(arr[j][N - i - 1], end = '')
        print()
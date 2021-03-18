# SWEA 10993

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    system = [['K'] for _ in range(N)]
    for i in range(N):
        city = list(map(int, input().split()))
        arr.append(city)
    for i in range(N - 1):
        for j in range(1, N - i):
            power = arr[i + j][2] / ((arr[i][0] - arr[i + j][0]) ** 2 + (arr[i][1] - arr[i + j][1]) ** 2)
            if power > arr[i][2]:
                system[i] = str(j)
            
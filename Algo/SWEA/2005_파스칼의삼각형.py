# SWEA 2005

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    print('#{}'.format(tc))
    for i in range(N):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(arr[i - 1][j - 1] + arr[i - 1][j])
        print(*line)
        arr.append(line)
# SWEA 1954

def snail(N):
    # N * N 배열 초기화
    arr = [[0] * N for _ in range(N)]
    # 처음 위치 초기화
    x = 0
    y = -1
    # Up Down Left Right
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    value = 1
    cnt = N
    while cnt > 0:
        for i in range(4):
            while (1):
                ax = x + dx[i]
                ay = y + dy[i]
                if ax >= 0 and ax < N and ay >= 0 and ay < N:
                    if arr[ax][ay] == 0:
                        arr[ax][ay] = value
                        value += 1
                        # 현재위치 변경
                        x, y = ax, ay
                    else:
                        break
                else:
                    break
        cnt -= 2
    return arr

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = snail(N)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(res[i][j], end = ' ')
        print()
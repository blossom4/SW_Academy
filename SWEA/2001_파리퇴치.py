# SWEA 2001

def max_fly(arr, N, M):
    # i, j index로 영역 내부를 돌고,
    # k, l index로 파리채 내부를 돈다.
    max_value = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total_sum = 0
            for k in range(M):
                for l in range(M):
                    total_sum += arr[i + k][j + l]
            if max_value < total_sum:
                max_value = total_sum
    return max_value

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = max_fly(arr, N, M)

    print('#{} {}'.format(tc, res))
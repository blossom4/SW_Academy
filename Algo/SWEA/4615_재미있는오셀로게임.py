# SWEA 4615

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    put = [list(map(int, input().split()))]
    arr= [[] for _ in range(N)]
    # 기본돌 세팅
    arr[(N // 2) - 1][(N // 2) - 1] = 2
    arr[(N // 2) - 1][N // 2] = 1
    arr[N // 2][(N // 2) - 1] = 1
    arr[N // 2][N // 2] = 2
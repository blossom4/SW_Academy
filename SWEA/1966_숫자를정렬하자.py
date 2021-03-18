# SWEA 1966

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))
    for i in range(N):
        for j in range(N - 1):
            if N_list[j] > N_list[j + 1]:
                temp = N_list[j]
                N_list[j] = N_list[j + 1]
                N_list[j + 1] = temp
    for i in range(N):
        N_list[i] = str(N_list[i])
    res = str.join(' ', N_list)
    print('#{} {}'.format(tc, res))
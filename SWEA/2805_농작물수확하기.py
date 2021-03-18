# SWEA 2805

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        S = input()
        temp = []
        for j in range(N):
            temp += [int(S[j])]
        arr.append(temp)
    profit = 0
    for i in range(N):
        if i <= N // 2:
            for j in range((N - 1) // 2 - i, (N + 1) // 2 + i):
                profit += arr[i][j]
        else:
            for j in range(i - (N // 2), N - (i - (N // 2))):
                profit += arr[i][j]
    print('#{} {}'.format(tc, profit))

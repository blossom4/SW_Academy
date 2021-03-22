# 2439

N = int(input())
for i in range(N):
    for j in range(N):
        if j >= N - 1 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
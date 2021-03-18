# SWEA 2063

N = int(input())
N_list = list(map(int, input().split()))
for i in range(N):
    for j in range(N - 1):
        if N_list[j] > N_list[j + 1]:
            temp = N_list[j]
            N_list[j] = N_list[j + 1]
            N_list[j + 1] = temp
print(N_list[N // 2])
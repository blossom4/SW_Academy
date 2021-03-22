# 10871

N, X = map(int, input().split())
list_N = list(map(int, input().split()))
res = []
for i in range(N):
    if list_N[i] < X:
        res += [list_N[i]]
print(*res)
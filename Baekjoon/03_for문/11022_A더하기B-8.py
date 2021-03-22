# 11022

T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(tc, A, B, A + B))
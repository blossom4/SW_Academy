# SWEA 6019

T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    t = D / (A + B)
    total_d = t * F
    print('#{} {}'.format(tc, total_d))
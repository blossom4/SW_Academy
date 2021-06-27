# SWEA 11387

T = int(input())
for tc in range(1, T + 1):
    D, L, N = map(int, input().split())
    total_damage = 0
    for i in range(N):
        next_D = D * (1 + i * L * 0.01)
        total_damage += next_D
    print('#{} {}'.format(tc, int(total_damage)))
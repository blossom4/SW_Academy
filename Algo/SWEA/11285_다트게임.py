# SWEA 11285

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    r_list = []
    total_score = 0
    for i in range(N):
        x, y = map(int, input().split())
        r = (x ** 2 + y ** 2) ** 0.5
        if r <= 20:
            total_score += 10
        elif r <= 40:
            total_score += 9
        elif r <= 60:
            total_score += 8
        elif r <= 80:
            total_score +=  7
        elif r <= 100:
            total_score += 6
        elif r <= 120:
            total_score += 5
        elif r <= 140:
            total_score += 4
        elif r <= 160:
            total_score += 3
        elif r <= 180:
            total_score += 2
        elif r <= 200:
            total_score += 1
    print('#{} {}'.format(tc, total_score))
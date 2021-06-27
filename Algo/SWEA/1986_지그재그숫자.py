# SWEA 1986

def zigzag_num(N):
    total_num = 0
    for i in range(1, N + 1):
        if i % 2:
            total_num += i
            print(1)
        else:
            total_num -= i
            print(2)
    return total_num

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = zigzag_num(N)

    print('#{} {}'.format(tc, res))
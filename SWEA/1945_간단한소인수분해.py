# SWEA 1945

def int_factorization(N):
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    cnt_d = 0
    cnt_e = 0
    cnt_list = []
    while N % 2 == 0:
        N //= 2
        cnt_a += 1
    cnt_list.append(str(cnt_a))
    while N % 3 == 0:
        N //= 3
        cnt_b += 1
    cnt_list.append(str(cnt_b))
    while N % 5 == 0:
        N //= 5
        cnt_c += 1
    cnt_list.append(str(cnt_c))
    while N % 7 == 0:
        N //= 7
        cnt_d += 1
    cnt_list.append(str(cnt_d))
    while N % 11 == 0:
        N //= 11
        cnt_e += 1
    cnt_list.append(str(cnt_e))
    res = str.join(' ', cnt_list)
    return res

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = int_factorization(N)
    print('#{} {}'.format(tc, res))
# SWEA 1288

def count_sheep(N):
    num = [0 for i in range(10)]
    cnt = 0
    temp = N
    k = 1
    while (1):
        while N > 0:
            num[N % 10] += 1
            N //= 10
        for i in range(10):
            if num[i] == 0:
                k += 1
                N = temp * k
                break
            elif i == 9:
                cnt += 1
                return cnt * temp
        cnt += 1
        

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = count_sheep(N)
    print('#{} {}'.format(tc, res))
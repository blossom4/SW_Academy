# SWEA 4408

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * 201
    for i in range(N):
        a = (arr[i][0]+1)//2
        b = (arr[i][1]+1)//2
        if a > b:
            a, b  = b, a
        for j in range(a, b+1):
            check[j] += 1
    print(f'#{tc} {max(check)}')
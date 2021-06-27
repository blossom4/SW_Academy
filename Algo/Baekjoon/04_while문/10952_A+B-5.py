# 10952

# 무한루프
while 1:
    A, B = map(int, input().split())
    # A, B 모두 0이면 무한루프 탈출
    if A == 0 and B == 0:
        break
    print(A + B)
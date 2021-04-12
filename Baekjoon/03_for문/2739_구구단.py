# 2739

# int형 input을 받는다.
n = int(input())
# 1~10의 범위에서 반복
for i in range(1, 10):
    # X * X = XX 형태의 구구단 출력
    print('{} * {} = {}'.format(n, i, n * i))
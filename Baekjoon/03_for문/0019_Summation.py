# 8393

# int형 input을 받는다.
n = int(input())
total = 0
# 1~n까지 반복
for i in range(1, n + 1):
    # total에 index를 더한다.
    total += i
# total 출력
print(total)
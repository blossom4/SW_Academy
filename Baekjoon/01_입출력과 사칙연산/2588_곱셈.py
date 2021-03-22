# 2588

# 두번에 걸쳐서 int형 input을 받는다.
a = int(input())
b = int(input())
# 각각의 연산 결과 출력
print(a * (b % 10))
print(a * ((b // 10) % 10))
print(a * (b // 100))
print(a * b)
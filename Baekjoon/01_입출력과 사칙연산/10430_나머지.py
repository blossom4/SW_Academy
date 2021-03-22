# 10430

# ' '을 잘라낸 여러가지 input 정보를 int형으로 받는다.
a, b, c = map(int, input().split(' '))
# 각각의 연산 결과들을 출력
print((a + b) % c)
print(((a %c ) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
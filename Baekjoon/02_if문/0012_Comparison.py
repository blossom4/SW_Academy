# 1330

# ' '을 잘라낸 여러가지 input 정보를 int형으로 받는다.
a, b = map(int, input().split(' '))
# 비교 결과에 따라 기호를 출력
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
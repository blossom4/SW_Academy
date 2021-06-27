# 14681

# int형 input을 받는다.
x = int(input())
y = int(input())
# x, y가 모두 양수이면 1사분면
if x > 0 and y > 0:
    print(1)
# x가 양수, y가 음수이면 4사분면
elif x > 0 and y < 0:
    print(4)
# x가 음수, y가 양수이면 2사분면
elif x < 0 and y > 0:
    print(2)
# x가 음수, y가 음수이면 3사분면
elif x < 0 and y < 0:
    print(3)
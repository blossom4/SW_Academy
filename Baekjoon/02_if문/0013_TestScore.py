# 9498

# int형 input을 받는다.
score = int(input())
# 점수에 따른 알파벳 출력
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
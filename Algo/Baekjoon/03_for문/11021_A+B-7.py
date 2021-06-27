# 11021

# int형 input t를 받는다.
t = int(input())
res = []
# t만큼 반복
for i in range(t):
    # ' '을 기준으로 a, b 두 정수를 입력 받는다.
    a, b = map(int, input().split())
    # 두 수의 합을 res(list)에 추가
    summ = a + b
    res += [summ]
# res(list)에서 반복
for j in range(len(res)):
    # index와 그에 해당되는 res의 요소값을 출력
    print('Case #{}: {}'.format(j + 1, res[j]))
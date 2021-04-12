# 15552

import sys
# int형 input을 받는다.
t = int(input())
input_list = []
# t만큼 반복
for i in range(t):
    # sys모듈의 sys.stdin은 input()보다 속도가 빠르다.
    # ' '을 잘라낸 여러가지 input 정보를 int형으로 받고 list로 만든다.
    lst = list(map(int, sys.stdin.readline().split(' ')))
    # 만들어진 list를 input_list(list)에 합친다.
    input_list += lst
# input_list(list)의 길이를 2씩 묶어서 반복
for j in range(0, 2 * t, 2):
    # 0번 index부터 요소 두개씩 더한다.
    res = input_list[j] + input_list[j + 1]
    # 더하기 값 res 출력
    print(res)